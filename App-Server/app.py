from flask import Flask
from flask import request
import json
from os import listdir
from os.path import isfile, join
import copy
import subprocess

app = Flask(__name__)
baseurl = '/scanner'
MY_PATH = './../cache'

"""
    Gets the contents of a cached file
"""
def file_get_contents(filename):
    with open(filename) as f:
        return f.read()

"""
    Consumes the raw input of cryptoguard and returns the rule violations as a
    comma seperated list
"""
def parse_data(str):
    if "***Violated Rule" not in str:
        #no rules were violated
        return "No vulnerabilities found"
    arr = str.split("***Violated Rule ")
    r = []
    #get the rules as numbers
    for i in range (1, len(arr)):
        r.append(arr[i].split(":")[0].strip())
    #remove the duplicates
    rules = []
    for i in r:
        if i not in rules:
            rules.append(i)
    ret_val = ""
    count = 0
    for i in rules:
        if i == "1":
            ret_val += "Found broken crypto schemes"
        elif i == "2":
            ret_val += "Found Broken Hash Function"
        elif i == "3":
            ret_val += "Used constant keys in code"
        elif i == "4":
            ret_val += "Uses Untrusted TrustManager"
        elif i == "5":
            ret_val += "Used default key size in method"
        elif i == "6":
            ret_val += "Uses untrusted HostNameVerifier"
        elif i == "8a":
            ret_val += "Used 1000 iterations for PBE"
        elif i == "9":
            ret_val += "Found constant salts in code"
        elif i == "12":
            ret_val += "Does not manually verify the hostname"
        elif i == "13":
            ret_val +="Untrusted PRNG"
        elif i == "14":
            ret_val +="Used Predictable KeyStore Password"
        else:
            ret_val += "Vulnerability (not decoded, " + i + ")"

        if count + 1 < len(rules):
            ret_val += ", "
        count += 1
    return ret_val


@app.route('/')
@app.route(baseurl + '/', methods=['GET'])
def hello():
    return "hello world"


@app.route(baseurl + '/a', methods=['POST'])
def home():
    j = json.loads(request.data)["nameValuePairs"]
    apk_names = []
    #create a list of the properly formatted app names
    for i in j:
        apk_names.append(i + "_v" + j[i])
    #get the files in the cache directory
    cache_apps = [f for f in listdir(MY_PATH) if isfile(join(MY_PATH, f))]
    #create two lists: one where analysis has already been run and one where analysis needs to be return
    done = []
    run = copy.deepcopy(apk_names)
    for i in apk_names:
        for j in cache_apps:
            if i in j:
                #this analysis was cached
                run.remove(i)
                done.append(i)
                print(i, " (cache)")
    analysis_results = {}
    #get the analysis that has already been run first
    for i in done:
        analysis_results[i] = parse_data(str(file_get_contents(MY_PATH + "/" + i + ".txt")))
    #then run the analysis on the remaining cache_apps
    avail_apks = listdir(MY_PATH + "/../apks")
    for i in run:
        apk_name = i + ".apk"
        if apk_name not in avail_apks:
            print(i, " (no apk)")
            analysis_results[i] = "apk not supported"
            continue
        args = "java -jar ../cryptoguard-ccs-submission/main/build/libs/main.jar \"apk\" \"../apks/" + i + ".apk\" \"\" 1"
        proc = subprocess.Popen(args, stdout = subprocess.PIPE, shell = True)
        stdout, stderr = proc.communicate();
        status = proc.wait()
        f = open("../cache/" + i + ".txt", "w")
        f.write(str(stdout))
        f.close()
        analysis_results[i] = parse_data(str(stdout))
        if status != 0:
            print("there was an error running the analysis on: ", i)
            continue
        #write the analysis to the cache folder
        print(i, " (analysis run)")
    analysis_results = json.dumps(analysis_results)
    return analysis_results



if __name__ == "__main__":
    app.run(debug=True)
