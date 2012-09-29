$('#DisplayAllExercises').click(function() {
	$.get('/Exercise/displayAll/', function(data) {
		displayExercises(data)
		});
});

$('.exercise').click(function() {
	id = $(this).data('exerciseid');
	$.get('/Exercise/load/' + id, function(exercise) {
		loadExercise(exercise);
		});
});

var loadExercise = 	function(exercise) {
	var methodBody = exercise.MethodBody
	var methodCalls = exercise.MethodCalls

	var methodCallText = "";
	var index = 0;

	var methodResult = function() {
		index = index + 1;
		return 'unitTestResult' + index + ' = ';
	};

	for (var method in methodCalls) {
		var methodAnswer = ' #expected: ' + methodCalls[method]
		methodCallText += methodResult() + method.toString() + methodAnswer + "\n";
	};

	$('#PythonCode').text(methodBody);
	$('#MethodCalls').text(methodCallText);

	$('#Exercises').dialog('close')
};

var displayExercises = function(data) {
	$('#Exercises').html(data);
	$('#Exercises').dialog();
	
}