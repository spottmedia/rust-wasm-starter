# rust-wasm-starter

A minimalistic rust+wasm boilerplate with a working dev instance for hacking around and sample deployments.
Based on https://developer.mozilla.org/en-US/docs/WebAssembly/rust_to_wasm

## Provisioning

So that you don't have to fiddle with installing rust and npm dependencies manually


### Requirements

* lxd (should ship with latest Ubuntus by default)

### Setup

if not done before, do `lxd init`. Normally just confirming defaults will suffice,
unless willing to delve into details of lxd/lxc specifically.


#### Starting new containers

Then the actual provisioning with

    cd provisioning
    ./bootstrap_provisioning.sh
    . provisioningenv/bin/activate
    molecule converge

#### Re-provisioning

to update container to the latest from the repo
    molecule converge

to scrap the machine and bring it back up
    molecule destroy && molecule converge

the latter might be useful if you've broken the dev container too much and want a fresh start


### Accessing the dev environment

    lxc exec dev-rust-wasm-starter-18-04 bash