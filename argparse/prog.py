# Copyright 2014 Ferry. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Test code for argparse"""

__author__ = 'fewang@microstrategy.com (Fengwei Wang)'

import argparse

parser = argparse.ArgumentParser(description='calculate X to the power of Y')
group = parser.add_mutually_exclusive_group()
group.add_argument('-v', '--verbose', action='store_true',
                   help='increase output verbosity')
group.add_argument('-q', '--quiet', action='store_true')
parser.add_argument('x', type=int, help='the base')
parser.add_argument('y', type=int, help='the exponent')
args = parser.parse_args()
answer = args.x ** args.y

if args.quiet:
    print answer
elif args.verbose:
    print '{} to the power {} equals {}'.format(args.x, args.y, answer)
else:
    print '{}^{} == {}'.format(args.x, args.y, answer)
