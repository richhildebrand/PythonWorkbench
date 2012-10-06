$('#SimpleDemo').click(function() {
	var methodBody = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	loadAllData(methodBody, "");
});

$('#ClearAll').click(function() {
	loadAllData("", "");
});

var loadAllData = function(methodBody, unitTestsText, unitTests) {
	$('#ResultData').val("");
	$('#PythonCode').val(methodBody);
	$('#MethodCalls').val(unitTestsText);
	loadTestGridData($('#TestResultGrid ol.expectedResultColumn'), unitTests)
};

$('#startDebugging').click(function() {
	var pythonCode = { pythonCode: $('#PythonCode').val(), unitTests: $('#MethodCalls').val() };
	$.get('/student/startDebugging', pythonCode, function(data) {
		displayResultData(data)
	});
});

$("#TakeStep").click(function() {
  $.get('/student/takeStep', function(data) {
		displayResultData(data)
	});
});

var displayResultData = function(data) {
	$('#ResultData').text(data.exception + data.localVars + data.lineNumber);
	var testResults = data.testResults;
	if (testResults) {
		for (testResult in testResults) {
			 $('#TestResultGrid ol.testColumn').append('<li>' + testResult.toString() + '</li>');
			 $('#TestResultGrid ol.actualResultColumn').append('<li>' + testResults[testResult] + '</li>');
		};
	};
};

var displayListData = function(target, dataSet) {
	if (dataSet) {
		for (data in dataSet) {
			 target.append('<li>' + dataSet[data] + '</li>');
		};
	};
};


var loadTestGridData = function(target, tests) {
	if (tests) {
		for (test in tests) {
			 $('#TestResultGrid ol.testColumn').append('<li>' + test.toString() + '</li>');
			 target.append('<li>' + tests[test] + '</li>');
		};
	};
};