<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-6">
                <div class="card-header font-weight-bold h6" style="text-transform: capitalize; text-align:center">
                    List of all Users
                </div>
                <div class="card card-accent-primary" >
                    <div class="card-block mx-auto">
                        <div class="row">
                            <br/>
                        </div>
                        <div  >
                        <table class="table table-bordered table-striped">
                            <thead class="font-weight-bold">
                                <tr>
                                    <td>Name</td>
                                    <td>User Id</td>
                                    <td>Role</td>
                                    <td style="width:10%"></td>
                                </tr>
                                <tr>
                                    <td><input v-model="searchKey['UserName']" class="searchBox" ></td>
                                    <td><input v-model="searchKey['UserId']" class="searchBox" ></td>
                                    <td></td>
                                    <td></td>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(user, userIndex) in filteredAndSortedList(allUsers)" :key="userIndex" >
                                    <td> {{user.UserName}} </td>
                                    <td> {{user.UserId}} </td>
                                    <td>
                                        <input type="checkbox" name="userRole" v-model="user.UserRole.isAdmin">Admin 
                                        <input type="checkbox" name="userRole" v-model="user.UserRole.isOwner">Owner 
                                        <input type="checkbox" name="userRole" v-model="user.UserRole.isDataProvider">DataProvider 
                                    </td>
                                    <td>
                                        <button type="submit" class="btn btn-success pull-right"  title = "Save" @click="saveUserRoles(user)">
                                            <i class="fa fa-save"></i> 
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-2">
                <div class="card-header font-weight-bold h6" style="text-transform: capitalize; text-align:center">
                    List of Areas
                </div>
                <div class="card card-accent-primary">
                    <div class="card-block mx-auto">
                        <div class="row"><br/></div>
                        <table class="table table-bordered table-striped">
                            <thead class="font-weight-bold">
                                <tr>
                                    <td>Name</td>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(area, areaIndex) in kpiAreas" :key="areaIndex" >
                                    <td>{{area.Area}}</td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="form-group" v-if="newArea">
                            <input style="width:70%"  v-model="newKPIArea" placeholder="Area">
                            <button type="submit" class="btn btn-success"  title = "Save Area" @click="saveNewArea()" >
                                <i class="fa fa-save"></i> 
                            </button>
                        </div>
                        <button type="submit" class="btn btn-primary pull-right"  title = "New Area" @click="addNewArea()" >
                            <i v-if="!newArea" class="fa fa-plus-square-o"></i> 
                            <i v-else class="fa fa-minus-square-o"></i>
                        </button>
                    </div>
                </div>
            </div>
            <div class="col-md-2">
                <div class="card-header font-weight-bold h6" style="text-transform: capitalize; text-align:center">
                    List of Units
                </div>
                <div class="card card-accent-primary">
                    <div class="card-block mx-auto">
                        <div class="row"><br/></div>
                        <table class="table table-bordered table-striped">
                            <thead class="font-weight-bold">
                                <tr>
                                    <td>Units</td>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(unit,unitIndex) in kpiUnits" :key="unitIndex" >
                                    <td>{{unit.Unit}}</td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="form-group" v-if="newUnit">
                            <input style="width:70%"  v-model="newKPIUnit" placeholder="Unit">
                            <button type="submit" class="btn btn-success"  title = "Save Unit" @click="saveNewUnit()" >
                                <i class="fa fa-save"></i> 
                            </button>
                        </div>
                        <button type="submit" class="btn btn-primary pull-right"  title = "New Unit" @click="addNewUnit()" >
                            <i v-if="!newUnit" class="fa fa-plus-square-o"></i> 
                            <i v-else class="fa fa-minus-square-o"></i>
                        </button>
                    </div>
                </div>
            </div>
            <div class="col-md-2">
                <div class="card-header font-weight-bold h6" style="text-transform: capitalize; text-align:center">
                    List of Categories
                </div>
                <div class="card card-accent-primary">
                    <div class="card-block mx-auto">
                        <div class="row"><br/></div>
                        <table class="table table-bordered table-striped">
                            <thead class="font-weight-bold">
                                <tr>
                                    <td>Categories</td>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(category, categoryIndex) in kpiCategories" :key="categoryIndex" >
                                    <td>{{category.Category}}</td>
                                </tr>
                            </tbody>
                        </table>
                        <div class="form-group" v-if="newCategory">
                            <input style="width:70%"  v-model="newKPICategory" placeholder="Category">
                            <button type="submit" class="btn btn-success"  title = "Save Category" @click="saveNewCategory()" >
                                <i class="fa fa-save"></i> 
                            </button>
                        </div>
                        <button type="submit" class="btn btn-primary pull-right"  title = "New Category" @click="addNewCategory()" >
                            <i v-if="!newCategory" class="fa fa-plus-square-o"></i> 
                            <i v-else class="fa fa-minus-square-o"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>

import axios from 'axios';

/* eslint-disable */
export default {
    data: function() {
        return{
            allUsers:[],
            searchKey: { UserId : '',UserName: ''},
            sortKey: '',
            kpiAreas : {},
            newArea: false,
            newKPIArea: '',
            sortOrder: 1,
            kpiUnits: {},
            newUnit: false,
            newKPIUnit: '',
            kpiCategories: {},
            newCategory: false,
            newKPICategory: ''
        }
    },
    mounted: function() {
        this.getAllUsers();
        this.getKPIAreas();
        this.getKPIUnits();
    },

    methods: {
        getAllUsers:function(){
            const path = 'api/users';
            axios.get(path)
            .then(response => {
                this.allUsers = response.data.Users;
            })
            .catch(error => {
                console.log(error);
            });
        },

        saveUserRoles: function(user)
        {
            const path = 'api/saveUserRole';
            axios.post(path, user)
            .then(response => {
                if(response.data.status == 1 ){
                    this.raiseToastMessage(response.data.message,'success','fa-user-plus');
                }
                else
                {
                    var message = "Unable to save User Role";
                    this.raiseToastMessage(message,'error','fa-user-plus');
                }
            })
            .catch(error => {
                console.log(error);
                var message = "Unable to save User Role";
                this.raiseToastMessage(message,'error','fa-user-plus');
            })
        },

        getKPIAreas: function() {
            const path = 'api/kpiareas';
            axios.get(path)
            .then(response => {
                this.kpiAreas = response.data.KPIAreas;
            })
            .catch(error => {
                console.log(error);
            })
        },

        getKPICategories: function() {
            const path = 'api/kpicategories';
            axios.get(path)
            .then(response => {
                this.kpiCategories = response.data.KPICategories;
            })
            .catch(error => {
                console.log(error);
            })
        },

        getKPIUnits: function() {
            const path = 'api/kpiunits';
            axios.get(path)
            .then(response => {
                this.kpiUnits = response.data.KPIUnits;
            })
            .catch(error => {
                console.log(error);
            })
        },

        addNewUnit: function(){
            this.newUnit = !this.newUnit;
        },

        saveNewUnit:function(){
            if(this.newKPIUnit.length>0)
            {
                var that = this;
                axios.post("api/saveKPIUnit", {'Unit': this.newKPIUnit})
                .then(response => {
                     if(response.data.status == 1 ){
                        that.raiseToastMessage(response.data.message, 'success', 'fa-tasks');
                        this.getKPIUnits();
                        this.newUnit = false;
                        this.newKPIUnit = "";
                    }
                    else{
                        that.raiseToastMessage(response.data.message, 'error', 'fa-tasks');
                    }
                })
                .catch(error => {
                    console.log(error);
                });
            }
        },

        addNewArea: function(){
            this.newArea = !this.newArea;
        },

        saveNewArea:function(){
            if(this.newKPIArea.length>0)
            {
                var that = this;
                axios.post("api/saveKPIArea", {'Area': this.newKPIArea})
                .then(response => {
                     if(response.data.status == 1 ){
                        that.raiseToastMessage(response.data.message, 'success', 'fa-tasks');
                        this.getKPIAreas();
                        this.newArea = false;
                        this.newKPIArea = "";
                    }
                    else{
                        that.raiseToastMessage(response.data.message, 'error', 'fa-tasks');
                    }
                })
                .catch(error => {
                    console.log(error);
                });
            }
        },

        addNewCategory: function(){
            this.newCategory = !this.newCategory;
        },

        saveNewCategory:function(){
            if(this.newKPICategory.length>0)
            {
                var that = this;
                axios.post("api/saveKPICategory", {'Category': this.newKPICategory})
                .then(response => {
                     if(response.data.status == 1 ){
                        that.raiseToastMessage(response.data.message, 'success', 'fa-tasks');
                        this.getKPICategories();
                        this.newCategory = false;
                        this.newKPICategory = "";
                    }
                    else {
                        that.raiseToastMessage(response.data.message, 'error', 'fa-tasks');
                    }
                })
                .catch(error => {
                    console.log(error);
                });
            }
        },

        filteredAndSortedList : function(itemList) {
            var searchKey = this.searchKey;
            var sortKey = this.sortKey;
            var order = this.sortOrder;
            var list = itemList;
            if (!list) return;
            var that = this;

            if (searchKey) {
                list = list.filter(function (row) {
                    return Object.keys(searchKey).every(function(key) {
                        var searchText = searchKey[key];
                        if(!searchText || searchText.length <= 0 ) return true;                            
                        var value = (key.indexOf('.') > -1) ? that.getValueByPath(row, key) : row[key];
                        return  String(value).toLowerCase().indexOf(searchKey[key].toLowerCase()) > -1;
                    })
                })
            }
            if (sortKey) {
                list = list.slice().sort(function (a, b) {
                    a = (sortKey.indexOf('.') > -1) ? that.getValueByPath(a, sortKey) : a[sortKey];
                    b = (sortKey.indexOf('.') > -1) ? that.getValueByPath(b, sortKey) : b[sortKey];
                    return (a === b ? 0 : a > b ? 1 : -1) * order
                })
            }
            return list;
        }
    }
}
</script>

<style>

.modal-body {
    overflow-x: hidden;
}
.modal-header {
    padding: 15px;
}
.form-control {
    padding: 5px;
}
.searchBox {
    height: 21px;
    width: 100%;
    padding: 1px 3px;
    font-size: 12px;
    line-height: 1.5;
    border-radius: 7px;
    font-weight: normal;
    display: block;
    color: #607d8b;
    background-color: #fff;
    background-image: none;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, 0.15);
    transition: border-color ease-in-out 0.15s, box-shadow ease-in-out 0.15s;
}

</style>