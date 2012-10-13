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

var loadTestGridData = function() {
	if (UnitTests) {
		$('#TestResultGrid ol').empty();
		for (var unitTest in UnitTests) {
			$('#TestResultGrid ol.testColumn').append('<li>' + unitTest.toString() + '</li>');
			$('#TestResultGrid ol.expectedResultColumn').append('<li>' + UnitTests[unitTest].expectedResult + '</li>');
			$('#TestResultGrid ol.actualResultColumn').append('<li>' + UnitTests[unitTest].actualResult + '</li>');
		}
	}
};