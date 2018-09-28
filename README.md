Role bacula_storage
===================

Installation and configuration of the Bacula storage.

Role Variables
--------------

[variables](https://github.com/sedovandrew/ansible-role-bacula-storage/blob/master/defaults/main.yml)

Example Playbook
----------------

    - hosts: servers
      roles:
         - role: sedovandrew.bacula_storage
           become: true
           bacula_storage_name: StorageName
           bacula_director_name: DirectorName
           bacula_director_password: StoragePassword
           bacula_storage_devices:
             - name: FileDevice
               media_type: File
               archive_device: /bacula_storage
               label_media: "yes"
               random_access: "Yes"
               automatic_mount: "yes"
               removable_media: "no"
               always_open: "no"

Testing
-------

    molecule test

License
-------

BSD

Author Information
------------------

Sedov Andrey - sedoy80@gmail.com
