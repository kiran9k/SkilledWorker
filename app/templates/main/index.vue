<template>
    <div class="container-fluid">

       <div class="row text-center mb-1 mt-3">
            <h1 class="headingText">Skilled Worker</h1>
            <p>Find your ideal worker for Fulltime or Parttime job.</p>
        </div>
        <div class="row mb-2 mt-3">
        </div>
        <div class="row ">
            <div class="col-md-8 col-lg-8  col-sm-8 col-md-offset-2 col-sm-offset-2 col-lg-offset-2">
                <div class="jumbotron">
                <div class="row mb-1">
                    
                        <div class="col-md-5 col-sm-5 col-lg-5 search ">
                             <span class="fa fa-search"></span>
                             <input type="text" class="form-control " name="skill" v-model="searchData.skill"  placeholder="Enter Skill">
                        </div>
                        <div class="col-sm-5 col-md-5 col-lg-5 search">
                            <span class="fa fa-search"></span>
                            <input type="text" class="form-control" name="location" v-model="searchData.location"  placeholder="Enter Location">
                        </div>
                        
                        <button type="submit" class="btn btn-primary col-md-2 col-sm-2" @click="search()">Search</button>
                        
                    
                </div>
                </div>
            </div>
        </div>
        <div class="row mt-3">

        </div>
        <div class="row mb-3 mt-3 ">
            <div class="col-md-10 col-lg-10 col-sm-10 col-md-offset-1 col-sm-offset-1 col-lg-offset-1">
                <div class="tab">
                    <button class="tablinks" v-bind:class ="{ selectedTab: 'topWorkers'?'selectedTab':'' }" @click="showtab('topWorkers')">Top Workers</button>
                    <button class="tablinks" @click="showtab('skills')">Skills</button>
                </div>
                <table class="table table-bordered showWorkers" v-if ="selectedTab == 'topWorkers'">
                    <tr>
                        <td v-for="searchResult in searchResults1" class="col-md-3 col-sm-3 col-lg-3 col-xs-3">
                            <div class="col-md-5 col-lg-5 col-sm-5 col-xs-5">
                                <div class="row">
                                <div class="art index-art profile-art">
                                    <img v-bind:src="'images/'+searchResult.image" width="100%" >
                                </div>
                                </div>
                            </div>
                            <div class="col-md-6 col-lg-6 col-sm-6  col-xs-5 col-md-offset-1 col-xs-offset-1 col-sm-offset-1 col-lg-offset-1">
                                <div class="row "><h5 class="h5label" ><a href="#" @click="showProfiles(searchResult.userEmail)" >{{searchResult.name}}</a></h5></div>
                                <div class="row mt-1"><h6 class="h6label text-justify text-secondary">{{searchResult.skillSet}}</h6></div>
                                <div class="row "><h6 class="h6label">{{searchResult.location}}</h6></div>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td v-for="searchResult in searchResults2" class="col-md-3 col-sm-3 col-lg-3">
                            <div class="col-md-5 col-lg-5 col-sm-5 col-xs-5">
                                <div class="row">
                                <div class="art index-art profile-art">
                                    <img v-bind:src="'images/'+searchResult.image" width="100%" >
                                </div>
                                </div>
                            </div>
                            <div class="col-md-6 col-lg-6 col-sm-6  col-xs-6 col-md-offset-1 col-xs-offset-1 col-sm-offset-1 col-lg-offset-1">
                                <div class="row "><h5 class="h5label" ><a href="#" @click="showProfiles(searchResult.userEmail)" >{{searchResult.name}}</a></h5></div>
                                <div class="row mt-1"><h6 class="h6label text-justify text-secondary">{{searchResult.skillSet}}</h6></div>
                                <div class="row "><h6 class="h6label">{{searchResult.location}}</h6></div>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td v-for="searchResult in searchResults3" class="col-md-3 col-sm-3 col-lg-3">
                            <div class="col-md-5 col-lg-5 col-sm-5">
                                <div class="row">
                                <div class="art index-art profile-art">
                                    <img v-bind:src="'images/'+searchResult.image" width="100%" >
                                </div>
                                </div>
                            </div>
                            <div class="col-md-6 col-lg-6 col-sm-6  col-md-offset-1 col-sm-offset-1 col-lg-offset-1">
                                <div class="row "><h5 class="h5label" ><a href="#" @click="showProfiles(searchResult.userEmail)" >{{searchResult.name}}</a></h5></div>
                                <div class="row mt-1"><h6 class="h6label text-justify text-secondary">{{searchResult.skillSet}}</h6></div>
                                <div class="row "><h6 class="h6label">{{searchResult.location}}</h6></div>
                            </div>
                        </td>
                    </tr>
                </table>

                <table class="table table-bordered showWorkers" v-if ="selectedTab == 'skills'">
                </table>
            </div>
        </div>
        <div class="row mt-3">
        </div>
        <div class="row mb-2 mt-3">
            <div class="col-md-10 col-lg-10 col-sm-10 col-md-offset-1 col-lg-offset-1 col-sm-offset-1">
                <h3>We help you to find the best worker</h3>
                <p>Maecenas varius dolor ut ipsum vehicula congue. Nam accumsan erat risus, sed tempus magn ultrices vel. Donec facilisis odio dui, in vestibulum sem euismod sit amet. Cras egestas failisis nisl, non hendrerit nunc convallis ut. Aliquam quis consequat leo, eu sodales lorem.</p>
            </div>
        </div>
    </div>
</template>
<script>
 import router from '../router'
export default {
  data:function(){
      return{
          searchData:{
              skill:'',
              location:''
          },
          searchResults1:[],
          searchResults2:[],
          searchResults3:[],
          selectedTab:'topWorkers'
      }
  },
  created:function(){
      this.userProfiles();
  },
  methods:{
    search:function(){
        router.replace({ name: "Search" ,params: { skill: this.searchData.skill,location: this.searchData.location }});
    },
    showtab:function(value){
        this.selectedTab = value;
    },
    userProfiles:function()
    {
        
        //get current skill and Location
        var self= this;
        axios.post("api/searchJobs",{skill:'',location:''})
            .then(function(data){
                self.searchResults1 = data['data'].slice(1, 5);
                self.searchResults2 = data['data'].slice(5, 9);
                self.searchResults3 = data['data'].slice(9, 13);
            })
            .catch(function(error){
                console.log(error);
            });
    },
    showProfiles:function(emailId){
        router.replace({ name: "ShowProfile" ,params: {email:emailId}});
    },
        
  }
}
</script>