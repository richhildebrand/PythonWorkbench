var workbenchViewModel  = new kendo.data.ObservableObject({
	UnitTests: new Array(),

	reset: function() {
		var tests = this.get("UnitTests");
		while (tests.length > 0) {
			tests.pop();
		}
	},

	loadExpectedResults: function(tests) {
	this.reset()
	unitTests = this.get("UnitTests"); 
		for (var test in tests) {
			unitTests.push(new UnitTest(test, tests[test]));
		}
	},

	loadActualResults: function(tests) {
		unitTests = this.get("UnitTests");
		for (test in tests) { 
						var targetTest = _.find(unitTests, function(possibleTest) { 
							return possibleTest.name === test; 
						});
						targetTest.actualResult = tests[test];
		}; 
	},

	loadTestGridData: function() {
		unitTests = this.get("UnitTests")
		if (unitTests) {
			$('#TestResultGrid ol').empty();
			for (var i=0; i<unitTests.length; i++) {
				$('#TestResultGrid ol.testColumn').append('<li>' + unitTests[i].name + '</li>');
				$('#TestResultGrid ol.expectedResultColumn').append('<li>' +unitTests[i].expectedResult + '</li>');
				$('#TestResultGrid ol.actualResultColumn').append('<li>' + unitTests[i].actualResult + '</li>');
			}
		}
	}
});