/*
 * View model for Omisk
 *
 * Author: olemin
 * License: AGPLv3
 */
$(function() {
    function miskViewModel(parameters) {
      var self = this;
      self.isOperational = ko.observable();
      self.isOperational.subscribe(function(newValue) {
        $('#navbarLedDropdown').prop('disabled', !newValue);
        });
      self.fromCurrentData = function (data) {
          self._processStateData(data.state);
      };

      self.fromHistoryData = function (data) {
          self._processStateData(data.state);
      };

      self._processStateData = function (data) {
        //console.log("miskViewModel:",data.flags);
        self.isOperational(data.flags.operational);
      };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: miskViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies:["printerStateViewModel"],
        elements: ["#navbar_plugin_misk"]
    });
});
