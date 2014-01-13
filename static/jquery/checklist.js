
var currId = 0;
stepType; //Taken from createList.html, contains all step types



function addCreateStep(idNum){
	
	var stepNum = document.createElement("label");
	stepNum.className = "col-md-1 form-control";
	stepNum.innerHTML = idNum+1;
	
	var stepInput = document.createElement("input");
	stepInput.name = "name";
	stepInput.className = "form-control";
	stepInput.id = "newStepId"+idNum;
	
	var selectType = document.createElement("select");
	selectType.className = "form-control";
	for (var i=0;i<stepType.length;i++)
	{ 
		var option = document.createElement("option");
		option.text = stepType[i];
		selectType.appendChild(option);
	}
	
	var description = document.createElement("input");
	description.className = "form-control";
	
	
	var formGroup = document.createElement("div");
	formGroup.className = "form-group form-inline";
	formGroup.id = "groupStepId"+idNum;
	formGroup.appendChild(stepNum);
	formGroup.appendChild(stepInput);
	formGroup.appendChild(selectType);
	formGroup.appendChild(description);
	
	
	var createStepsDiv = document.getElementById("create-steps");
	
	createStepsDiv.appendChild(formGroup);
};

function deleteStep(){
	var createSteps = document.getElementById("create-steps");
	createSteps.removeChild(document.getElementById("groupStepId"+currId));
}





addCreateStep(currId);

$("#removeStep").click(function() {
	deleteStep();
	currId --;
});

$("#addStep").click(function() {
	currId ++;						 
	addCreateStep(currId);
	
	
});


