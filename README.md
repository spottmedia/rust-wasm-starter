# rust-wasm-starter

A minimalistic rust+wasm boilerplate with a working dev instance for hacking around and sample deployments.
Based on https://developer.mozilla.org/en-US/docs/WebAssembly/rust_to_wasm

## Provisioning

So that you don't have to fiddle with installing rust and npm dependencies manually.

Uses `Ansible`, `Ansible Galaxy` and `Molecule`

### Requirements

* lxd (should ship with latest Ubuntus by default)

### Setup

if not done before, do `lxd init`. Normally just confirming defaults will suffice,
unless willing to delve into details of lxd/lxc specifically.


#### Starting new containers

Then the actual provisioning (and integration testing) with

    cd provisioning
    ./bootstrap_provisioning.sh
    . provisioningenv/bin/activate
    molecule converge && molecule verify

#### Re-provisioning

just update machine

    molecule converge && molecule verify

scrap the machine and bring it back up

    molecule destroy && molecule converge && molecule verify

^ the latter might be useful if you've broken the dev container too much and want a fresh start


## Instaling the wasm stack

Once provisioned the resulting container will have all minimal core toolset installed already,
feel free to adjust as you go:

* rustc
* rustup
* cargo
* wasm-pack
* node
* npm
* nginx
* ngrok

all the above are symlinked back to he global `/bin` path so will be accessible from virtually
every possible location and worker (including cron)

### Access dev environment


    lxc exec dev-rust-wasm-starter-18-04 bash


note the root of the project will be mounted under `/var/www/rust-wasm-starter/` on the container, so you can use
the host system's IDE for development and then issue commands on the lxc machine to take effect if needed.


## Running the hello world sample

    cd examples/hello-wasm/site
    npm install
    nohup npm run serve > /tmp/hello-wasm-output.log &
    # should open 0.0.0.0:8080 on lxc with the app running
    # issue `lxc list` to figure out which IP your container was assigned

    # optionally to expose the app via ngrok publicly
    # in case you are using it nested within other vms
    ngrok http 8080

## Adding own projects

the most basic sample:

    cp examples/hello-wasm new-project
    # do the creative coding in the /src
    wasm-pack build

then carry on customizing and integrating. Refer to https://developer.mozilla.org/en-US/docs/WebAssembly/rust_to_wasm
for more details on the approach given here.
