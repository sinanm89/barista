Vagrant::Config.run do |config|
    config.vm.define "barista" do |config|
        config.vm.box = "trusty64"
        # config.vm.box_url = "http://rahatol.com/static/boxes/trusty64.box"
        # Try to get different ports for different VMs
        config.vm.forward_port 80, 8081
        config.vm.forward_port 8000, 8001
        config.vm.network :bridged
        config.vm.network :hostonly, "33.33.33.100"
        # Customizations
        config.vm.host_name = "ubuntu.local"
        config.vm.customize ["modifyvm", :id, "--rtcuseutc", "on"]
        config.vm.customize ["modifyvm", :id, "--cpus", 2]
        config.vm.customize ["modifyvm", :id, "--memory", 1024]
        config.vm.customize ["modifyvm", :id, "--pae", "on"]
        config.vm.customize ["modifyvm", :id, "--name", "barista"]
        config.ssh.max_tries = 100
        # nfs is faster than otherwise
        config.vm.share_folder("vagrant-root", "/vagrant", ".", :nfs => true)
    end
end
