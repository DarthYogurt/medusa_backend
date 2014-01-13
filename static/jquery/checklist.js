
var currId = 0;
stepType; //Taken from createList.html, contains all step types



function addCreateStep(idNum){
	
	var stepNum = document.createElement("label");
	stepNum.className = "col-md-1 ";
	stepNum.innerHTML = idNum+1;
	
	var stepName = document.createElement("input");
	stepName.name = "name";
	stepName.className = "col-md-4";
	stepName.placeholder = "name of step";
	stepName.id = "newStepId"+idNum;
	
	var selectType = document.createElement("select");
	selectType.className = "col-md-2";
	for (var i=0;i<stepType.length;i++)
	{ 
		var option = document.createElement("option");
		option.text = stepType[i];
		selectType.appendChild(option);
	}
	
	var description = document.createElement("input");
	description.placeholder = "description";
	description.className = "col-md-4";
	
	
	var formGroup = document.createElement("div");
	formGroup.className = "row";
	formGroup.id = "groupStepId"+idNum;
	formGroup.appendChild(stepNum);
	formGroup.appendChild(stepName);
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


