# Kinetic Gateway Checks
# flopach, Cisco, 2019
# Apache License 2.0
import requests
import time

# CONFIGURATION
# Put here your variables.
# the API needs to have at least the following permissions:
# Gateway Management RW, Organization Management RO
api_token = "token" #API for the Kinetic cloud
organization_id = 0000 #Insert your Organization ID
api_url_base = "https://eu.ciscokinetic.io/api/v2/" #EU or
api_url_base = "https://us.ciscokinetic.io/api/v2/" #US

#headers
headers = {"Content-Type": "application/json",
           "Authorization": "Token {0}".format(api_token)}

def getgateways():
    r = requests.get(api_url_base+"organizations/{}/gate_ways".format(organization_id), headers=headers)
    if r.status_code == requests.codes.ok:
        output = r.json()
        #Get information from each gateway
        for x in range(len(output["gate_ways"])):
            serialno = output["gate_ways"][x]["uuid"]
            gwname = output["gate_ways"][x]["name"]
            gwmodel = output["gate_ways"][x]["model"]
            connected = output["gate_ways"][x]["field_director_state"]
            print("{} - {} ({},{})".format(connected, gwname,gwmodel,serialno,))
        sumup = output["summary"]["up"] #get the summary
        sumdown = output["summary"]["down"]
        print("Total UP: {} | Total DOWN: {}".format(sumup,sumdown))
    else:
        print("Error {}. Message: {}".format(r.status_code, r.content))

def gatewayconnectivity():
    r = requests.get(api_url_base+"organizations/{}/gate_ways".format(organization_id), headers=headers)
    if r.status_code == requests.codes.ok:
        output = r.json()
        jobs = {}
        # get for each gateway the ID and make the Kinetic cloud do the connectivity test
        # Kinetic cloud is sending back a job ID which will be stored together with the name of the gateway
        for x in range(len(output["gate_ways"])):
            r_gw = requests.post(api_url_base+"/gate_ways/{}/diagnostics/ping_ios".format(output["gate_ways"][x]["id"]), headers=headers)
            output_gw = r_gw.json()
            try:
                jobs[x] = [output_gw["job_id"], output["gate_ways"][x]["name"]]
                print("Sending ping to gateway {}".format(x))
            except:
                print("Gateway error: Can't create job.")
        #wait for the responses of the gateway
        print("Please wait 30 seconds for responses...")
        time.sleep(30)
        print("Results:")
        # ask the Kinetic cloud again what is the status of the job, which is the status of the job
        for key, value in jobs.items():
            r_job = requests.get(api_url_base + "/jobs/{}".format(value[0]), headers=headers)
            output_job = r_job.json()
            print("{} : {}".format(value[1],output_job["message"]["message"]))
    else:
        print("Error {}. Message: {}".format(r.status_code, r.content))

if __name__ == "__main__":
    print("Welcome! 0: Gateway summary | 1: Instant gateway connectivity")
    var = input("Enter: ")
    if var == "0":
        getgateways()
    elif var == "1":
        gatewayconnectivity()
    else:
        print("Wrong input")
    print("End")