<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-12 col-lg-12">
                <div class="well well-lg row">
                    <div>
                        <div class="col-md-5 search">
                            <span class="fa fa-search"></span>
                            <input type="text" class="form-control-sm" style="width: 100%" v-model="searchData.skill" placeholder="Enter Skill">
                        </div>
                        <div class="col-md-5 search">
                            <span class="fa fa-search"></span>
                            <input type="text" class="form-control-sm" style="width:100%;" v-model="searchData.location" placeholder="Enter Location">
                        </div>
                        <div class="col-md-1 col-lg-1">
                            <button type="submit" style="width: 100%" class="btn btn-primary" @click="search()">Search</button>
                        </div>

                    </div>
                </div>
            </div>
        </div>
        <div class="row mt-1 mb-3 " v-if="searching">
            <div class="col-md-3 col-lg-3">
                <fieldset style="border: 1px black solid">
                    <legend class="text-center" align="center" style="border:none;width: 150px;">Search Filter</legend>
                    <div class="col-md-12 col-md-offset-0 col-lg-12">
                        <!--<select class="form-control input-select" id="sel1">
                            <option value="" disabled selected>Job Title</option>
                        </select>-->
                        <select class="form-control input-select" id="sel2" v-model="pageSettings.fullTime">
                            <option value=""  selected>FullTime/PartTime</option>
                            <option value="FullTime">FullTime</option>
                            <option value="PartTime">PartTime</option>
                        </select>
                        <select class="form-control input-select" id="sel3" v-model="pageSettings.salary">
                            <option value="" selected>All Salary</option>
                            <option value="0-20" selected>&lt;20$</option>
                            <option value="21-50" selected>21$-50$</option>
                            <option value="51-100" selected>51$-100$</option>
                            <option value="101-200" selected>101$-200$</option>
                            <option value="201-500" selected>201$-500$</option>
                            <option value="501-10000" selected>501$&gt;</option>
                        </select>
                        <select class="form-control input-select" v-model="pageSettings.location" id="sel4">
                            <option value=""  selected>All Location</option>
                            
                            <option v-for="location in filterOptions.locations" :value="location" >
                                {{location}}
                            </option>
                        </select>
                        <label class="input-select">Gender
                            <div class="radio disabled">
                                <label class="radio-inline"><input type="radio" name="optradio" value="" v-model="pageSettings.gender">All</label>
                                <label class="radio-inline"><input type="radio" name="optradio" value="Male" v-model="pageSettings.gender">Male</label>
                                <label class="radio-inline"><input type="radio" name="optradio" value="Female" v-model="pageSettings.gender">Female</label>
                            </div>
                        </label>
                        <select class="form-control input-select" id="sel5" v-model="pageSettings.ageLimit">
                            <option value="" selected>No Age Limit</option>
                            <option value="0-20" >&lt;20</option>
                            <option value="21-30" >21-30</option>
                            <option value="31-40" >31-40</option>
                            <option value="41-50" >41-50</option>
                            <option value="51-100" >50&gt;</option>
                        </select>
                        <!--<label class="input-select">Rating<br/>
                            <div class="form-group">
                                <label for="rating" style="float: none;display: inline-block; ">0</label>
                                <input type="range" style="float: none;display: inline-block;" min="1" max="100" value="50" name="rating" class="slider form-control" id="myRange">
                                <label for="rating" style="float: none;display: inline-block;">5</label>
                            </div>

                        </label>-->
                        <div class="input-select text-center mt-2 mb-2">
                            <button type="submit" class="btn btn-primary" @click="filteredSearch()">Submit</button>
                            <button type="submit" class="btn btn-danger" @click="loadFilters()">Reset</button>
                        </div>
                    </div>
                </fieldset>
                </div>
                <div class="col-md-9 col-lg-9">
                    <fieldset style="border: 1px black solid">
                        <legend class="text-center" align="center" style="border:none;width: 150px">Search Result</legend>
                        <div class="container-fluid">
                            <div class="row mb-0"  v-if="searchResults.length > 0">
                                <div class="col-md-3 col-lg-3">
                                    {{paginate.showing}} out of {{paginate.totalCount}}
                                </div>
                                <div class="col-md-4 col-lg-4 text-center text-dark">
                                    Sort By
                                    <select v-model="pageSettings.sortBy" @change="reorderList(pageSettings.sortBy)">
                                        <option value="name">Name</option>  
                                        <option value="price">Price</option>
                                        <option value="location">Location</option>

                                    </select>
                                </div>
                                <div class="col-md-3 col-lg-3 pull-right">
                                    Per Page Result
                                    <select v-model="pageSettings.perPageResult" @change="navigate(1)">
                                        <option value="10">10</option>
                                        <option value="50">50</option>
                                        <option value="100">100</option>
                                    </select>
                                </div>
                            </div>
                            <div class="_1UoZlX row" v-else >
                                <div class="_3wU53n">
                                    No Result Found. Please try searching again.
                                </div>
                            </div>
                            <div class="row">
                                <hr>
                            </div>
                            <div class="_1UoZlX row" v-for="searchResult in searchResults">
                                <div class="_3SQWE6">
                                    <div class="_1OCn9C">
                                        <div>
                                            <div class="_3BTv9X" style="height: 100px; width:100px;">
                                                <img class="_1Nyybr  _30XEf0" alt="searchResult.name" v-bind:src="'images/'+searchResult.image">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="_1-2Iqu row">
                                    <div class="col-md-7">
                                        <div class="_3wU53n">{{searchResult.name}} &nbsp;&nbsp;
                                        <!--    <span class="fa fa-star checked"></span>
                                            <span class="fa fa-star checked"></span>
                                            <span class="fa fa-star checked"></span>
                                            <span class="fa fa-star"></span>
                                            <span class="fa fa-star"></span>-->
                                        </div>
                                        <div class="OiPjke">{{searchResult.location}}</div>

                                        <div class="_3ULzGw">
                                            Skill Description:
                                            <ul class="vFw0gD">
                                                <li class="tVe95H">{{searchResult.skillSet}}</li>
                                            </ul>
                                        </div>
                                        <div class="OiPjke">
                                            <a href="#" @click="showProfiles(searchResult.userEmail)">View Complete Detail </a>
                                        </div>
                                        <!--<div class="OiPjke">Last Update:{{datetime}}</div>-->
                                    </div>
                                    <div class=" col-md-2 ">
                                        <div class="_6BWGkk">
                                            <button type="button" class="btn btn-primary">Hire</button>
                                            <button type="button" class="btn btn-primary">Save</button>
                                        </div>
                                        <div class="_6BWGkk mt-1">
                                            <div class="_1uv9Cb">
                                                <div class="_1vC4OE _2rQ-NK">${{searchResult.price}}</div>
                                                <div class=" _2GcJzG">Per Hour</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="row vertical-center-row">
                                <ul class="pagination col-md-5 col-lg-5 col-md-offset-4 pagination-lg">
                                    <li v-for="page in paginate.pages"> 
                                        <a href="#" @click="navigate(page)">{{page}}</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </fieldset>
                </div>
            </div>

        </div>
        
    </div>
</template>
<script>
    import router from '../router'
    export default{
        data:function(){
            return {
                searchData : {
                    skill:'',
                    location : ''
                },
                searchResults:[],
                allSearchResults:[],
                pageSettings:{
                    perPageResult:10,
                    sortBy:'name',
                    fullTime:'',
                    gender:'',
                    ageLimit:'',
                    rating:'',
                    salary:'',
                    location:''
                },
                filterOptions:{
                    locations:[]
                },
                paginate:{
                    pages:[],
                    totalCount:'',
                    showing:'',
                },
                searching : false
            }
        },
        created:function(){
            this.searchData.skill = typeof(this.$route.params.skill) ==='undefined'?'':this.$route.params.skill;
            this.searchData.location = typeof(this.$route.params.location) === 'undefined'?'':this.$route.params.location;
            this.search();
            this.loadFilters();
        },
        methods:{
            search:function()
            {

                //get current skill and Location
                var self= this;
                axios.post("api/searchJobs",{skill:this.searchData.skill,location:this.searchData.location})
                    .then(function(data){
                        self.searching =  true;
                        self.allSearchResults = data['data'];
                        self.paginate.totalCount = self.allSearchResults.length;
                        self.paginate.pages=[];
                        self.reorderList(self.pageSettings.sortBy);
                        for(var i=1;i<=Math.ceil(self.paginate.totalCount/self.pageSettings.perPageResult);i++)
                            self.paginate.pages.push(i);
                    })
                    .catch(function(error){
                        console.log(error);
                    });
            },

            loadFilters:function(){
                var self=this;
                axios.get("api/listFilterJobs")
                .then(function(data){
                    self.filterOptions.locations = data['data']['location'];
                })
                .catch(function(error){
                    console.log(error);
                });
            },

            filteredSearch:function(){
                var self= this;
                axios.post("api/fileredSearchJobs",
                {skill:this.searchData.skill,location:this.pageSettings.location,age:this.pageSettings.ageLimit,
                gender:this.pageSettings.gender,salary:this.pageSettings.salary,fulltime:this.pageSettings.fullTime})
                    .then(function(data){
                        self.allSearchResults = data['data'];
                        self.paginate.totalCount = self.allSearchResults.length;
                        self.reorderList(self.pageSettings.sortBy);
                        self.paginate.pages=[];
                        for(var i=1;i<=Math.ceil(self.paginate.totalCount/self.pageSettings.perPageResult);i++)
                            self.paginate.pages.push(i);
                        
                    })
                    .catch(function(error){
                        console.log(error);
                    });
            },
            
            byProperty : function(prop) {
                return function(a,b) {
                    if (typeof a[prop] == "number") {
                        return (a[prop] - b[prop]);
                    } else {
                        return ((a[prop] < b[prop]) ? -1 : ((a[prop] > b[prop]) ? 1 : 0));
                    }
                };
            },

            navigate:function(index){
                index = index-1;
                var from_range = parseInt(index*this.pageSettings.perPageResult);
                var to_range = parseInt(index *(this.pageSettings.perPageResult))+parseInt(this.pageSettings.perPageResult);
                this.searchResults =this.allSearchResults.slice(from_range,to_range);
                this.paginate.showing=from_range+1+"-"+to_range;
            },

            reorderList:function(key){
                this.allSearchResults.sort(function(a, b) {
                    if(key =="price")
                        return a[key] - b[key];
                    else
                    {
                        var x = a[key].toLowerCase();
                        var y = b[key].toLowerCase();
                        return x < y ? -1 : x > y ? 1 : 0;
                    }
                });
                this.navigate(1);
            },
            showProfiles:function(emailId){
                console.log("emaild :"+emailId);
                router.replace({ name: "ShowProfile" ,params: {email:emailId}});
            },
        }
    }
</script>