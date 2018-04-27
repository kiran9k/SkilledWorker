/*jshint esversion: 6 */

import Vue from 'vue';
import router from './router';

import Toastr from 'vue-toastr';
import VeeValidate from 'vee-validate';
import Toasted from 'vue-toasted';

import axios from 'axios/dist/axios.min';

import modal from '../templates/main/Modal.vue';

import common from './common';


import Multiselect from 'vue-multiselect';


window.common = common;
window.axios = axios;

Vue.component(modal.name, modal);
Vue.component('vue-toastr', Toastr);

Vue.component('multiselect', Multiselect)


Vue.config.productionTip = false;


Vue.use(VeeValidate);
Vue.use(Toasted)

// options to the toast
let options = {
    position: 'top-right',
    duration: 5000,
    action:{
        text : 'X',
        onClick : (e, toastObject) => {
          toastObject.goAway(0);
        }
    },
    type :'info',
    theme:'bubble',
    iconPack : 'fontawesome',
    icon : 'fa-plus-circle'
};

// Toast Registration
Vue.toasted.register('toastMessage',
    (payload) => {
        options.type = payload.type;
        options.icon = payload.icon;
        return payload.message;
    },
    options
)

Vue.mixin({
    methods: {
        raiseToastMessage: function(comment,type,icon) {
            // Raises toast Message given Comment, type and Icon
            Vue.toasted.global.toastMessage({
                message : comment,
                type: type,
                icon: icon
            });
        },

        checkColorRange: function (actValue, tarValue, colorFrom, colorTo) {
            if (colorFrom && colorTo) {
                if (actValue >= this.parseColor(colorFrom, tarValue) && actValue <= this.parseColor(colorTo, tarValue))
                    return true;
            } else if (colorFrom) {
                if (actValue >= this.parseColor(colorFrom, tarValue))
                    return true;
            } else if (colorTo) {
                if (actValue <= this.parseColor(colorTo, tarValue))
                    return true;
            } else
                return false;
        },

        getColorPriority: function (KPIColor, tarValue) {
            return [{
                    'color': 'Red',
                    'value': this.parseColor(KPIColor.RedTo, tarValue) - this.parseColor(KPIColor.RedFrom, tarValue)
                },
                {
                    'color': 'Yellow',
                    'value': this.parseColor(KPIColor.YellowTo, tarValue) - this.parseColor(KPIColor.YellowFrom, tarValue)
                },
                {
                    'color': 'Green',
                    'value': this.parseColor(KPIColor.GreenTo, tarValue) - this.parseColor(KPIColor.GreenFrom, tarValue)
                }
            ];
        },

        setColorPriority: function (tarValue, colorCodes, colorPriority, KPIColor) {
            var appliedColor = '';
            // Sorting the color priorities in ascending order of total range of values
            colorPriority.sort(function (a, b) {
                return a.value - b.value;
            });
            if (colorCodes.length === 2) {
                var firstColor = colorCodes.pop();
                var secondColor = colorCodes.pop();
                var firstColorValue;
                var secondColorValue;
                colorPriority.forEach(colorProp => {
                    if (firstColor === colorProp.color)
                        firstColorValue = colorProp.value;
                    else
                        secondColorValue = colorProp.value;
                });
                if (firstColorValue <= secondColorValue)
                    appliedColor = 'set' + firstColor;
                else
                    appliedColor = 'set' + secondColor;
            } else {
                appliedColor = 'set' + colorPriority[0].color;
            }
            return appliedColor;
        },

        checkColor: function (kpiValue, KPIColor) {
            if (KPIColor && kpiValue.ActualValue) {
                var color = '';
                var actValue = parseFloat(kpiValue.ActualValue);
                var tarValue = parseFloat(kpiValue.TargetValue);
                var colorCodes = [];
                if (this.checkColorRange(actValue, tarValue, KPIColor.RedFrom, KPIColor.RedTo))
                    colorCodes.push('Red');
                if (this.checkColorRange(actValue, tarValue, KPIColor.YellowFrom, KPIColor.YellowTo))
                    colorCodes.push('Yellow');
                if (this.checkColorRange(actValue, tarValue, KPIColor.GreenFrom, KPIColor.GreenTo))
                    colorCodes.push('Green');
                // Color coding that does not overlap
                if (colorCodes.length < 1)
                    return color;
                else if (colorCodes.length === 1) {
                    color = 'set' + colorCodes;
                } else {
                    var colorPriority = this.getColorPriority(KPIColor, tarValue);
                    color = this.setColorPriority(tarValue, colorCodes, colorPriority, KPIColor);
                }
                return color;
            }
        },

        parseColor: function (colorString, target) {
            var value = 0;
            if (colorString.toLowerCase().indexOf('target') >= 0)
                colorString = colorString.replace(/target/i, target);
            // Checking the target + value, target + value% cases
            if (colorString.indexOf("+") > 0) {
                for (var x of colorString.split("+")) {
                    if (x.indexOf("%") > 0) {
                        x = parseFloat(x) * value / 100;
                    }
                    value = value + parseFloat(x);
                }
            }
            // Checking the target - value, target - value% cases
            else if (colorString.indexOf("-") > 0) {
                if (colorString.split("-")[0])
                    value = parseFloat(colorString.split("-")[0]);
                for (var x of colorString.split("-").slice(1, )) {
                    if (x.indexOf("%") > 0) {
                        x = parseFloat(x) * value / 100;
                    }
                    value = value - parseFloat(x);
                }
            } else {
                value = null;
                if (colorString)
                    value = parseFloat(colorString);                
            }
            return value;
        }
    }
});


var app = new Vue({
    router: router,
  }).$mount('#app');

