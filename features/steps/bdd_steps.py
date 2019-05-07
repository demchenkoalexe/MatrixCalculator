from behave import given, when, then, step
import json
from MatrixCalculator import *

@given('we have matrix calculator')
def step_impl(context):
	context.mc = MatrixCalculator()
	assert context.failed is False

@when('we have {A} as first matrix')
def step_impl(context, A): 
	context.matrixA = json.loads(A)

@when('we have {B} as second matrix')
def step_impl(context, B): 
	context.matrixB = json.loads(B)

@when('we have {num1:d} number')
def step_impl(context, num1): 
	context.num = num1

@then('the add result should be {C}')
def step_impl(context, C):
	assert context.mc.addTwoMatrix(context.matrixA, context.matrixB) == json.loads(C)

@then('the diff result should be {C}')
def step_impl(context, C):
	assert context.mc.diffTwoMatrix(context.matrixA, context.matrixB) == json.loads(C)

@then('the multi matrix by number result should be {C}')
def step_impl(context, C):
	assert context.mc.multiMatrixByNumber(context.matrixA, context.num) == json.loads(C)

@then('the transpose result should be {C}')
def step_impl(context, C):
	assert context.mc.transpose(context.matrixA) == json.loads(C)

@then('the multi result should be {C}')
def step_impl(context, C):
	assert context.mc.multiTwoMatrix(context.matrixA, context.matrixB) == json.loads(C)

