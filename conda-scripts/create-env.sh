#!/bin/sh

# MIT License

# Copyright (c) [year] [fullname]

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# !!!! DISCLAIMER and NOTICE: !!!!!
#
# This script is NOT for PRODUCTION use. It is intended only for personal and for educational purpose.
# The logic in this shell script (below) is not robust enough and therefor should not be used for commercial and PRODUCTION purposes. 
# If you intend to create conda environments for STAGING or PRODUCTION, please read the documentation of Conda/Anaconda and documentation of shell scripts to know how to create robust logic which can take different error handling scenario;s into account. 
# The author of this script will not be held responsible nor liable for ANY risk if this script is used for STAGING and PRODUCTION purposes.

ENV_YML_FILE=$1
conda env create -f $ENV_YML_FILE
