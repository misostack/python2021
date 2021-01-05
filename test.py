def assert_equals(test_result, expected_result, error=None):
	try:
		assert test_result == expected_result, "{} must be {}".format(test_result, expected_result)
		print("Passed : {} : {} : {}", test_result, expected_result, True)
	except Exception as e:
		if error:
			print(error)
		else:
			print("Failed : {} : {} : {}", test_result, expected_result, False)
		# print("Error {}".format(e))
	