from conditionblock import ConditionBlock

class ConditionStructure:

	def __init__(self, if_block, else_block, cond):
		self.if_block = if_block
		self.else_block = else_block
		self.cond = cond

	def isCondTrue():
		print("do if true")

# block1 = ConditionBlock("IF", "something", "action")
# block2 = ConditionBlock("ELSE", None, "action2")

# structure = ConditionStructure(block1, block2)

# structure.if_block.runAction()