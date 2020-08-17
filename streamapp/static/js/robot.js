Blockly.Blocks['sag'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldDropdown([["sag","sag"]]), "sag")
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
  
  Blockly.Python['sag'] = function(block) {
    var dropdown_sag = block.getFieldValue('sag');
    var number_adim_sayisi = block.getFieldValue('adim_sayisi');
    var number_hiz = block.getFieldValue('hiz');
    if (number_adim_sayisi >= 0 && number_hiz >=0){
      alert("kod")
    }
    return code;
  };

  Blockly.Blocks['sol'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldDropdown([["sol","sol"]]), "sol")
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

  Blockly.Python['sol'] = function(block) {
    var dropdown_sol = block.getFieldValue('sol');
    var number_adim_sayisi = block.getFieldValue('adim_sayisi');
    var number_hiz = block.getFieldValue('hiz');
    // TODO: Assemble Python into code variable.
    var code = '...\n';
    return code;
  };

  Blockly.Blocks['ileri'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldDropdown([["ileri","ileri"]]), "ileri")
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

  Blockly.Python['ileri'] = function(block) {
    var dropdown_ileri = block.getFieldValue('ileri');
    var number_adim_sayisi = block.getFieldValue('adim_sayisi');
    var number_hiz = block.getFieldValue('hiz');
    // TODO: Assemble Python into code variable.
    var code = 'SendRobot(ileri,';
    code = code + number_adim_sayisi;
    code = code + ',';
    code = code + number_hiz;
    code = code + ')'

    return code;
  };

  Blockly.Blocks['geri'] = {
    init: function() {
      this.appendDummyInput()
          .appendField(new Blockly.FieldDropdown([["geri","geri"]]), "geri")
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

  Blockly.Python['geri'] = function(block) {
    var dropdown_geri = block.getFieldValue('geri');
    var number_adim_sayisi = block.getFieldValue('adim_sayisi');
    var number_hiz = block.getFieldValue('hiz');
    // TODO: Assemble Python into code variable.
    var code = '...\n';
    return code;
  };