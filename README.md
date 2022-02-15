# Servplatform

Program with multiple functionalities to deploy and manage a linux container platform with 'lxc' and 'lxd'

## The program can be summarized with the extended help output of the program ('-ha' argument)
```
python3 main.py <parameters> <flags> <options> [command] <parameters> <flags> <options> [command] ...

  => main.py --> Despliega y controla una plataforma de servidores
     - commands:
        => deploy --> <void or integer between(1-5)> --> deploys a server platform with
                  the number of servers especified (if void, 2 servers are created). It
                  also initializes a load balancer that acts as a bridge between the
                  servers and a data base for storing data. Everything is connected by 2
                  virtual bridges 
           - options:
              => --image --> <alias or fingerprint> allows to specify the image of the
                        containers, by default ubuntu:18.04 is used 
              => --simage --> <alias or fingerprint> allows to specify the image of the
                        servers 
              => --name --> <server_names> allows to specify the names of the servers
              => --use --> <app_name> allows to specify the app that will be deployed in
                        the servers (if they are being runned) 
              => --lbimage --> <alias or fingerprint> allows to specify the image of the
                        load balancer 
              => --balance --> <algorithm_name> allows to specify the balance algorithm of
                        the load balancer (roundrobin, leastconn, source, ...). By default
                        'roundrobin' is used 
              => --port --> <port_number> changes the port where the load balancer is
                        listening (default -> 80)
              => --dbimage --> <alias or fingerprint> allows to specify the image of the
                        data base 
              => --client --> <void or client_name> creates a client connected to the load
                        balancer 
              => --climage --> <alias or fingerprint> allows to specify the image of the
                        client 
           - flags:
              => -l --> launches the containers 
              => -t --> opens the terminal window of the containers 
              => -m --> marks the servers index.html
        => start --> <void or container_names> runs the containers specified, if void all
                  containers are runned 
           - options:
              => --skip --> <names> skips the containers specified
              => --use --> <app_name> allows to specify the app that will be deployed in
                        the servers (if any server among the containers specified is being
                        started) 
           - flags:
              => -m --> marks the servers index.html
              => -t --> opens the terminal window of the containers 
        => stop --> <void or container_names> stops the containers currently running, if
                  void all containers are stopped 
           - options:
              => --skip --> <names> skips the containers specified
        => pause --> <void or container_names> pauses the containers currently running, if
                  void all containers are paused 
           - options:
              => --skip --> <names> skips the containers specified
        => delete --> <void or container_names> deletes the containers specified, if void
                  all containers are deleted (only servers and clients) 
           - options:
              => --skip --> <names> skips the containers specified
           - flags:
              => -y --> executes the action without asking confirmation 
        => destroy --> deletes every component of the platform created 
           - flags:
              => -y --> executes the action without asking confirmation 
        => servs --> allows to interact with the servers
           - commands:
              => run --> <void or server_name> starts the servers specified. If void, all
                        of them 
                 - options:
                    => --skip --> <names> skips the containers specified
                    => --use --> <app_name> allows to specify the app that will be
                              deployed in the servers 
                 - flags:
                    => -m --> marks the servers index.html
                    => -t --> opens the terminal window of the containers 
              => stop --> <void or server_name> stops the servers specified. If void, all
                        of them 
                 - options:
                    => --skip --> <names> skips the containers specified
              => pause --> <void or server_name> pauses the servers specified. If void,
                        all of them 
                 - options:
                    => --skip --> <names> skips the containers specified
              => add --> <void or number> creates the number of servers specified. If
                        void, one is created
                 - options:
                    => --name --> <names> allows to specify the names
                    => --image --> allows to specify the image
                    => --use --> <app_name> allows to specify the app that will be
                              deployed in the servers (if they are being runned) 
                 - flags:
                    => -l --> launches the containers 
                    => -m --> marks the servers index.html
                    => -t --> opens the terminal window of the containers 
              => rm --> <void or server_names> deletes the servers specified. If void all
                        are deleted
                 - options:
                    => --skip --> <names> skips the containers specified
                 - flags:
                    => -y --> executes the action without asking confirmation 
              => use --> <app_name> changes the app of the servers 
                 - options:
                    => --on --> <names> allows to specify the servers
              => mark --> <void or server_name> marks the app index.html of the servers
                        specified. If void, all of them 
                 - options:
                    => --skip --> <names> skips the containers specified
              => unmark --> <void or server_name> unmarks the app index.html of the
                        servers specified. If void, all of them 
                 - options:
                    => --skip --> <names> skips the containers specified
        => client --> allows to interact with the client
           - commands:
              => add --> creates a container with lynx installed in order to act as a
                        client
                 - options:
                    => --name --> allows to specify the name
                    => --image --> allows to specify the image
                 - flags:
                    => -l --> launches the containers 
                    => -t --> opens the terminal window of the containers 
              => rm --> removes the client
                 - flags:
                    => -y --> executes the action without asking confirmation 
        => loadbal --> allows to interact with the load balancer
           - commands:
              => add --> creates a container with haproxy installed in order to act as a
                        load balancer
                 - options:
                    => --image --> allows to specify the image
                    => --balance --> allows to specify the balance algorithm
                    => --port --> allows to specify the port of the container where
                              haproxy is going to be listening
                 - flags:
                    => -l --> launches the containers 
                    => -t --> opens the terminal window of the containers 
              => rm --> removes the load balancer
                 - flags:
                    => -y --> executes the action without asking confirmation 
              => set --> allows to change some varibales
                 - commands:
                    => algorithm --> <algorithm_name> changes the balance algorithm. Some
                              of the most common ones are 'roundrobin(default), leastconn,
                              source ...' 
                    => port --> <port_number> changes the port where the load balancer is
                              listening (default -> 80)
              => reset --> resets the configuration to the default one
        => database --> allows to interact with the data base
           - commands:
              => add --> creates a container with mongodb installed in order to act as a
                        data base
                 - options:
                    => --image --> allows to specify the image
                 - flags:
                    => -l --> launches the containers 
                    => -t --> opens the terminal window of the containers 
              => rm --> removes the data base
                 - flags:
                    => -y --> executes the action without asking confirmation 
        => repo --> allows to interact with the local repositories
           - commands:
              => apps --> allows to interact with the apps local repository
                 - commands:
                    => add --> <absolute_paths> adds 1 or more apps to the local
                              repository 
                       - options:
                          => --name --> <names> allows to specify the names
                       - flags:
                          => -d --> sets the first app specified as default
                    => rm --> <app_names> removes apps from the local repository
                       - flags:
                          => -y --> executes the action without asking confirmation 
                    => setdef --> <app_name> changes the default app of the servers
                    => unsetdef --> makes the default app to be none
                    => list --> lists the apps of repository
                    => clear --> clears the apps repository
                       - options:
                          => --skip --> <names> skips the apps specified
                       - flags:
                          => -y --> executes the action without asking confirmation 
        => show --> shows information about the program
           - commands:
              => state --> <void or machine_names> shows information about every
                        machine/component of the platform specified, if void, all are
                        showed 
              => diagram --> displays a diagram that explains the structure of the
                        platform 
              => info --> shows important information about how the platform is built and
                        deployed, and the requirements that the container images need to
                        fulfill, in order to fit into the platform (in case an specific
                        image is passed to the program) 
              => dep --> shows information about the external dependencies of the program 
        => term --> <void or container_names> opens the terminal of the containers
                  specified or all of them if no name is given 
        => publish --> <container_name> publish the image of the container specified 
           - options:
              => --alias --> allows to specify the alias of the image
     - flags:
        => -w --> 'warning mode', only shows warning and error msgs during execution 
        => -d --> 'debug mode' option for debugging. Shows debug msgs during execution 
        => -q --> 'quiet mode', doesn't show any msg during execution (only when an error
                  occurs) 
        => -s --> executes the code sequencially instead of concurrently 
 + Global Flags:
    -> -h --> shows overall information about a command or all of them if a valid one is
              not introduced
    -> -hc --> is the same as -h but with some predefined colors
    -> -ha --> is the same as -h but displaying all information
    -> -hca --> combines -h, -hc and -ha
```
