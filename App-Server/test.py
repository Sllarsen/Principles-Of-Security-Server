import subprocess

def main():
    args = "java -jar ../cryptoguard-ccs-submission/main/build/libs/main.jar \"apk\" \"../apks/HokieMobile_v2.2.0.apk\" \"\" 1"
    proc = subprocess.Popen(args, stdout = subprocess.PIPE, shell = True)
    stdout, stderr = proc.communicate();
    status = proc.wait()
    print("stdout: " + stdout)
    print("status:", status)


if __name__ == "__main__":
    main()
