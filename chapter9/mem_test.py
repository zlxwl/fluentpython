# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 下午5:02
# @Author  : Zhong Lei
# @FileName: mem_test.py
import importlib
import sys
import resource

NUM_VECTORS = 10 ** 7

if len(sys.argv) == 2:
    module_name = sys.argv[1].replace('.py', '')
    module = importlib.import_module(module_name)
else:
    print('Usage: {} <vector-module-to-test>'.format())
    sys.exit(1)

fmt = 'Selected Vector2d type: {.__name__}.{.__name__}'
print(fmt.format(module, module.Vector2d))

mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('creating {:,} Vector2d instances'.format(NUM_VECTORS))

vectors = [module.Vector2d(3.0, 4.0) for i in range(NUM_VECTORS)]
mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

print('Initial Ram usage {:14}'.format(mem_init))
print('  Final Ram usage {:14}'.format(mem_final))