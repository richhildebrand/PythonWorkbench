var UnitTests = new Array();

var UnitTest = function(expectedResult) {
	this.expectedResult = expectedResult;
	this.actualResult = "";
};

var loadExpectedResults = function(tests) {
	UnitTests = new Array();
	for (var test in tests) {
		UnitTests[test] = new UnitTest(tests[test]);
	}
};

var loadActualResults = function(tests) {
	for (var test in tests) {
		UnitTests[test].actualResult = tests[test];
	} 
};

