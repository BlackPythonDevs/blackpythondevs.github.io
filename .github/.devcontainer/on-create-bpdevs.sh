#!/bin/sh

rbenv install $(cat .ruby-version)
rbenv global $(cat .ruby-version)

PRISM_DIR=/usr/local/rvm/gems/default/gems/prism-0.17.1
export C_INCLUDE_PATH=$PRISM_DIR/include:$PRISM_DIR/ext:$C_INCLUDE_PATH
