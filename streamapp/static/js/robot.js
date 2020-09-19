Blockly.Blocks['yon'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown([["ileri","ileri"], ["geri","geri"],["sag","sag"], ["sol","sol"],  [{"src":"https://www.gstatic.com/codesite/ph/images/star_on.gif","width":15,"height":15,"alt":"*"},"OPTIONNAME"]]), "field_yon")
        .appendField(new Blockly.FieldNumber(0, 0), "adim_sayisi")
        .appendField("->Adım")
        .appendField(new Blockly.FieldNumber(0, 0), "hiz")
        .appendField("->Hız");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(123);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['yon'] = function(block) {
  var code = ""
  var dropdown_yon = block.getFieldValue('field_yon');
  var number_adim_sayisi = block.getFieldValue('adim_sayisi');
  var number_hiz = block.getFieldValue('hiz');

  if(dropdown_yon == "ileri"){
      code = 'Robot(ileri,';
  }

  else if (dropdown_yon == "geri"){
      code = 'Robot(geri,';
  }

  else if (dropdown_yon == "sag"){
      code = 'Robot(sag,';
  }

  else if (dropdown_yon == "sol"){
      code = 'Robot(sol,';
  }

  code = code + number_adim_sayisi;
  code = code + ',';
  code = code + number_hiz;
  code = code + ')'
  code = code + '\n';

  return code;
};

Blockly.Blocks['bekle'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldNumber(0), "waiting_time")
        .appendField("sn")
        .appendField(new Blockly.FieldLabelSerializable("bekle"), "bekle");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(180);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['bekle'] = function(block) {
var number_waiting_time = block.getFieldValue('waiting_time');
// TODO: Assemble Python into code variable.
var code = 'time.sleep(' + number_waiting_time + ')' + '\n';
return code;
};


Blockly.Blocks['adim_boyu'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldLabelSerializable("Adım Boyu"), "adim_boyu")
        .appendField(new Blockly.FieldNumber(0.1, 1), "adim_uzunlugu");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['adim_boyu'] = function(block) {
  var number_adim_uzunlugu = block.getFieldValue('adim_uzunlugu');
  // TODO: Assemble Python into code variable.
  var code = 'Robot(adimboyu,';
  code = code + number_adim_uzunlugu;
  code = code + ')'
  code = code + '\n';
  return code;
};

Blockly.Blocks['camera'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("kamera")
        .appendField(new Blockly.FieldDropdown([["yukarı","yukari"], ["aşağı","asagi"]]), "camy")
        .appendField(new Blockly.FieldNumber(0, 0, 750), "cameray")
        .appendField(new Blockly.FieldDropdown([["sağ","sag"], ["sol","sol"]]), "camx")
        .appendField(new Blockly.FieldNumber(0, 0, 750), "camerax");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Python['camera'] = function(block) {
  var dropdown_camy = block.getFieldValue('camy');
  var number_cameray = block.getFieldValue('cameray');
  var dropdown_camx = block.getFieldValue('camx');
  var number_camerax = block.getFieldValue('camerax');
  // TODO: Assemble Python into code variable.
  var code = '';
  if (dropdown_camy == "yukari") {
      code = code + 'Robot(cam,yukari,';
  }
  else if (dropdown_camy == "asagi") {
      code = code + 'Robot(cam,asagi,';
  }
  code = code + number_cameray;
  code = code + ')'
  code = code + '\n';

  if (dropdown_camx == "sag"){
      code = code + 'Robot(cam,sag,';
  }
  else if (dropdown_camx == "sol"){
      code = code + 'Robot(cam,sol,';
  }
  code = code + number_camerax;
  code = code + ')'
  code = code + '\n';

  return code;

};