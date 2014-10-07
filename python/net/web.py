from subprocess import check_output

def get_page (url):
        output=check_output(["wget", "-q", "-O", "-", url])
        return output
