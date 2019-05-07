from behave import given, when, then, step
import json
from MatrixCalculator import *

@given('we have matrix calculator')
def step_impl(context):
	context.mc = MatrixCalculator()
	assert context.failed is False

@when('we have {A} as first operand')
def step_impl(context, A): 
	context.matrixA = json.loads(A)

@when('we have {B} as second operand')
def step_impl(context, B): 
	context.matrixB = json.loads(B)

@then('the result should be {C}')
def step_impl(context, C):
	assert context.mc.addTwoMatrix(context.matrixA, context.matrixB) == json.loads(C)