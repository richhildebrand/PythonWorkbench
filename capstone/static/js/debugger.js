$('#SimpleDemo').click(function() {
	var methodBody = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	loadAllData(methodBody, "");
});

$('#ClearAll').click(function() {
	loadAllData("", "");
});

var loadAllData = function(methodBody, methodCalls) {
	$('#ResultData').val("");
	$('#PythonCode').val(methodBody);
	$('#MethodCalls').val(methodCalls);
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
		var fillTestAreaWith = "";
		for (testResult in testResults) {
			 $('#TestResultGrid ol.testColumn').append('<li>' + testResult.toString() + '</li>');
			 $('#TestResultGrid ol.actualResult').append('<li>' + testResults[testResult] + '</li>');
		};
		$('#ResultData').text(fillTestAreaWith);
	};
};