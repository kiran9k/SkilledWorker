export default {
    showMessage: function (toastr, msg, title, type) {
        //var toastr = this.$root.$refs.toastr;
        toastr.defaultProgressBar = false;
        toastr.defaultTimeout = 2000;
        toastr.title = title ? title : null;
        toastr.defaultPosition = "toast-top-right";
         if(type && type === 'e'){
            toastr.e(msg, title + " Error");
        } else {
            toastr.s(msg, title);
        }
    }
}
