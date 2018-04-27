<template>
    <div class="container-fluid">

       <div class="row text-center mt-2">
            <h1 class="headingText">Skilled Worker</h1>
            <p>Find your ideal worker for Fulltime or Parttime job.</p>
        </div>
        <div class="row">
            <div class="col-md-8 col-lg-8 col-md-offset-2">
                <div class="jumbotron">
                <div class="row mb-1">
                    
                        <div class="col-md-5 col-lg-5 ">
                        <input type="text" class="form-control" name="skill" v-model="searchData.skill"  placeholder="Enter Skill">
                        </div>
                        <div class="col-md-5 col-lg-5">
                        <input type="text" class="form-control" name="location" v-model="searchData.location"  placeholder="Enter Location">
                        </div>
                        
                        <button type="submit" class="btn btn-primary col-md-2" @click="search()">Search</button>
                        
                    
                </div>
                </div>
            </div>
        </div>
        <div class="row">

        </div>
        <div class="row mb-2 mt-3 ">
            <div class="col-md-10 col-lg-10 col-md-offset-1">

                <table class="table table-bordered">
                    <tr>
                        <td v-for="searchResult in searchResults1" class="col-md-3">
                            <div class="col-md-6 col-lg-6">
                                <div class="row">
                                <div class="art index-art profile-art">
                                    <img v-bind:src="'images/'+searchResult.image" >
                                </div>
                                </div>
                            </div>
                            <div class="col-md-6 col-lg-6">
                                <div class="row "><h5 class="h5label">{{searchResult.name}}</h5></div>
                                <div class="row mt-1"><h6 class="h6label text-justify text-secondary">{{searchResult.skillSet}}</h6></div>
                                <div class="row "><h6 class="h6label">{{searchResult.location}}</h6></div>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td v-for="searchResult in searchResults2" class="col-md-3">
                            <div class="col-md-6 col-lg-6">
                                <div class="row">
                                <div class="art index-art profile-art">
                                    <img v-bind:src="'images/'+searchResult.image" >
                                </div>
                                </div>
                            </div>
                            <div class="col-md-6 col-lg-6">
                                <div class="row "><h5 class="h5label">{{searchResult.name}}</h5></div>
                                <div class="row mt-1"><h6 class="h6label  text-secondary">{{searchResult.skillSet}}</h6></div>
                                <div class="row "><h6 class="h6label">{{searchResult.location}}</h6></div>
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td v-for="searchResult in searchResults3" class="col-md-3">
                            <div class="col-md-6 col-lg-6">
                                <div class="row">
                                <div class="art index-art profile-art">
                                    <img v-bind:src="'images/'+searchResult.image" >
                                </div>
                                </div>
                            </div>
                            <div class="col-md-6 col-lg-6">
                                <div class="row "><h5 class="h5label">{{searchResult.name}}</h5></div>
                                <div class="row mt-1"><h6 class="h6label text-justify text-secondary">{{searchResult.skillSet}}</h6></div>
                                <div class="row "><h6 class="h6label">{{searchResult.location}}</h6></div>
                            </div>
                        </td>
                    </tr>
                </table>

            </div>
        </div>
        <div class="row mb-2 mt-3">
            <div class="col-md-10 col-lg-10 col-md-offset-1">
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
      }
  },
  mounted:function(){
      this.userProfiles();
  },
  methods:{
    search:function(){
        router.replace({ name: "Search" ,params: { skill: this.searchData.skill,location: this.searchData.location }});
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
    }
        
  }
}
</script>