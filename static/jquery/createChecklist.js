
//Taken from createList.html, contains all step types
//stepType; 
//users;


var currId = 0;

function showUserOptions(){
	var userToNotifySelect = document.getElementById("userToNotify")
	
	for (var i=0; i<users.length;i++){
		var s = users[i];
		var id = s.substring( s.indexOf("-")+1, s.length);
		var name = s.substring(0,s.indexOf("-"))
		var option = document.createElement("option");
		option.name = "userToNotify" + id;
		option.value = id;
		option.text = id + " " + name;
		userToNotifySelect.appendChild(option);
		
	}
}

function addCreateStep(idNum){
	//STRAT FIRST ROW
	var stepNum = document.createElement("label");
	stepNum.innerHTML = idNum+1;
	var stepNumDiv = document.createElement("div");
	stepNumDiv.className = "col-sm-1";
	stepNumDiv.appendChild(stepNum);
	
	var stepName = document.createElement("input");
	stepName.name = "stepName"+idNum;
	stepName.className = "form-control";
	stepName.placeholder = "name of step";
	stepName.id = "newStepId"+idNum;
	var stepNameDiv = document.createElement("div");
	stepNameDiv.className = "col-sm-4";
	stepNameDiv.appendChild(stepName);
	
	var selectType = document.createElement("select");
	selectType.className = "form-control";
	selectType.name="stepType"+idNum;
	for (var i=0;i<stepType.length;i++)
	{ 
		var option = document.createElement("option");
		option.text = stepType[i];
		option.value = stepType[i];
		selectType.appendChild(option);
	}
	var selectTypeDiv = document.createElement("div");
	selectTypeDiv.className = "col-sm-2";
	selectTypeDiv.appendChild(selectType);
	
	var description = document.createElement("input");
	description.placeholder = "description";
	description.className = "form-control tab-to-add";
	description.id = "desc"+idNum
	description.name = "desc"+idNum
	var descriptionDiv = document.createElement("div");
	descriptionDiv.className = "col-sm-5";
	descriptionDiv.appendChild(description);
	
	var divRow = document.createElement("div");
	divRow.className = "row form-group";
	divRow.appendChild(stepNumDiv);
	divRow.appendChild(stepNameDiv);
	divRow.appendChild(selectTypeDiv);
	divRow.appendChild(descriptionDiv);
	//END FIRST ROW
	
	// Second level buttons, show hide external 
	var extraNoteRow = document.createElement("div");
	extraNoteRow.className = "row form-group";
	
	//hideCheckbox
	var noteColEmpty = document.createElement("div");
	noteColEmpty.className = "col-sm-1";
	
	var hideCol = document.createElement("div");
	hideCol.className = "col-sm-2";
	var hideDiv = document.createElement("div");
	hideDiv.className="checkbox";
	var hideLabel = document.createElement("label");
	hideLabel.innerHTML = "Hide ";
	var hideInput = document.createElement("input");
	hideInput.type = "checkbox";
	hideLabel.appendChild(hideInput);
	hideDiv.appendChild(hideLabel);
	hideCol.appendChild(hideDiv);
	
	//Required Checkbox
	var reqCheckboxCol = document.createElement("div");
	reqCheckboxCol.className = "col-sm-2";
	var reqCheckboxDiv = document.createElement("div");
	reqCheckboxDiv.className = "checkbox";
	var reqLabel = document.createElement("label");
	reqLabel.innerHTML = "Required";
	var reqInput = document.createElement("input");
	reqInput.type = "checkbox";
	reqInput.onclick = function (currId){
		test(currId);
	}
	
	
	reqLabel.appendChild(reqInput);
	reqCheckboxDiv.appendChild(reqLabel);
	reqCheckboxCol.appendChild(reqCheckboxDiv);

	extraNoteRow.appendChild(noteColEmpty);
	extraNoteRow.appendChild(hideCol);
	extraNoteRow.appendChild(reqCheckboxCol);
	
	var divCreateCol = document.createElement("div");
	divCreateCol.className = "col-sm-12";
	divCreateCol.id = "groupStepId"+idNum;
	
	divCreateCol.appendChild(divRow);
	divCreateCol.appendChild(extraNoteRow);
	
	document.getElementById("totalSteps").value=currId;
	var createStepsDiv = document.getElementById("create-steps");
	createStepsDiv.appendChild(divCreateCol);
};

function deleteStep(){
	var createSteps = document.getElementById("create-steps");
	createSteps.removeChild(document.getElementById("groupStepId"+currId));
	
}




showUserOptions();
addCreateStep(currId);
document.getElementById("totalSteps").value=currId+1;

$("#removeStep").click(function() {
	deleteStep();
	currId --;
	document.getElementById("totalSteps").value=currId+1;
});

$("#addStep").click(function() {
	currId ++;
	addCreateStep(currId);
	document.getElementById("totalSteps").value=currId+1;
});


function test(currId){
	console.log("outside");	
};

document.addEventListener('keydown', function(e){
                if( e.keyCode == '9' && e.srcElement.className.indexOf("tab-to-add") > 0 ){
                    currId ++;
					addCreateStep(currId);
					document.getElementById("totalSteps").value=currId+1;
                }
            }, false);
