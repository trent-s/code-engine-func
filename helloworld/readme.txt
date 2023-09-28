# inline function creation:

ibmcloud ce fn create --name helloworld --inline-code __main__.py --runtime python-3.11

# verify with:

ibmcloud ce fn get -n helloworld

# when done delete with:

ibmcloud ce fn delete -n helloworld
