c = connect.ConnectNoSSL(host="10.30.31.33", user="siddharth.shri", pwd='Sungard01')

datacenter = c.content.rootFolder.childEntity[0]
dictVmDetail = {}
dictDetail = {}

for folder in c.content.rootFolder.childEntity[0].vmFolder.childEntity:
	print(folder.name)
	for num in range(0, len(folder.childEntity)):
		print(folder.childEntity[num].name)
        

# Folders as keys and VMs under them as values        
for folder in c.content.rootFolder.childEntity[0].vmFolder.childEntity:
	dictDetail[folder.name] = [folder.childEntity[num].name for num in range(0, len(folder.childEntity))]
    
#List of VMs
for folder in c.content.rootFolder.childEntity[0].vmFolder.childEntity:
	for num in range(0, len(folder.childEntity)):
		vmList.append(folder.childEntity[num].name) 
        
#Raw VM details
for folder in datacenter.vmFolder.childEntity:
	for num in range(0, len(folder.childEntity)):
		vm = folder.childEntity[num]
		vmName = vm.name
		print(vmName)
		vcpu = vm.summary.config.numCpu
		guestOs = vm.summary.config.guestFullName
		mem = vm.summary.config.memorySizeMB
		print(vcpu)
		print(guestOs)
		print(mem)

#Dict of VMname as key and CPU, Mem, GuestOs, powerstate and IP as Values
for folder in datacenter.vmFolder.childEntity:
	for num in range(0, len(folder.childEntity)):
		vm = folder.childEntity[num]
		vmName = vm.name
		vcpu = vm.summary.config.numCpu
		guestOs = vm.summary.config.guestFullName
		mem = vm.summary.config.memorySizeMB
		datastore = vm.datastore[0].name
		powerState = vm.summary.runtime.powerState
		ipadd = vm.summary.guest.ipAddress
		dictVmDetail[vmName] = ([vcpu, mem, datastore, guestOs, powerState, ipadd]) 
        
        
dictVmDetail1 = {'Anand Kumar':{'Dev-test1': [2, 20000, 'Customer_41', 'CentOS 4/5/6/7 (64-bit)', 'poweredOn', None]}}


dictest1[datacenter.vmFolder.childEntity[0].name] = {datacenter.vmFolder.childEntity[0].childEntity[0].name:[datacenter.vmFolder.childEntity[0].childEntity[0].summary.config.numCpu, datacenter.vmFolder.childEntity[0].childEntity[0].datastore[0].name]}

