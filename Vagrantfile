Vagrant::Config.run do |config|
    config.vm.define :barista do |config|
        config.vm.box = "barista"
        config.vm.forward_port 80, 8081
        config.vm.forward_port 8000, 8005
        config.vm.network :bridged
        config.vm.network :hostonly, "33.33.33.10"
        config.vm.customize ["modifyvm", :id, "--rtcuseutc", "on"]
        config.ssh.max_tries = 100
        config.vm.share_folder("v-root", "/vagrant", ".", :nfs => true)
        config.vm.customize do |vm|
            vm.memory_size = 256
        end
    end
end
