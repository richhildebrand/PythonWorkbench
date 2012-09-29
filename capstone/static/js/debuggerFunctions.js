$('#DisplayExercises').click(function() {
	$.get('/Exercise/displayAll/', function(data) {
		displayExercises(data)
		});
});

$('#SimpleDemo').click(function() {
	methodBody = 'a = 3\nb = 4\nc = a + b\nd = a + b * c';
	methodCalls = ""
	$('#PythonCode').text(methodBody);
	$('#MethodCalls').text(methodCalls);
});

$('#ClearAll').click(function() {
	methodBody = ""
	methodCalls = ""
	$('#PythonCode').text(methodBody);
	$('#MethodCalls').text(methodCalls);
});

$('#startDebugging').click(function() {
	pythonCode = { pythonCode: $('#PythonCode').val() + '\n' + $('#MethodCalls').val() };
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
};	