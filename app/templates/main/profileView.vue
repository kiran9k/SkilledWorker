<template>
    <div class="container-fluid mb-2">
        <div class="row">
            <div class="col-md-8 col-lg-8 col-md-offset-2 mt-3 mb-3">
                <div class="page-wrap profile account well well-sm">
                    <div class="row">
                        <div class=" col-md-4 col-lg-4 col-md-offset-1 page-header">
                            <div class="row">
                                <div class="art solo-art profile-art">
                                    <img v-bind:src="'images/'+profileInfo.image">
                                </div>
                            </div>

                        </div>
                        <div class=" col-md-5 col-lg-5">
                            <div class="row mt-2 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Name</h5>
                                </div>
                                <div class="col-md-6">
                                    <span class="heading h6">{{profileInfo.name}}</span>

                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Sex</h5>
                                </div>
                                <div class="col-md-6">
                                    <span class="heading h6">{{profileInfo.sex}}</span>

                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">

                                    <h5 class="h5Label">Age</h5>
                                </div>
                                <div class="col-md-6">
                                    <span class="heading h6">{{profileInfo.age}}</span>

                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Job Type</h5>
                                </div>
                                <div class="col-md-6">
                                    <span class="heading h6">{{profileInfo.jobType}}</span>

                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Location</h5>
                                </div>
                                <div class="col-md-6">
                                    <span class="heading h6">{{profileInfo.location}}</span>

                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Skill Sets</h5>
                                </div>
                                <div class="col-md-6">
                                    <span class="heading h6">{{profileInfo.skillSet}}</span>

                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">

                                    <h5 class="h5Label">Price $(Per Hour)</h5>
                                </div>
                                <div class="col-md-6">
                                    <span class="heading h6">{{profileInfo.price}}</span>

                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Rating</h5>
                                </div>
                                <div class="col-md-6">
                                    <span class="heading h6">{{profileInfo.rating}}</span>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>

        </div>
    </div>
</template>
<<script>
export default {
  data:function () {
    return {
        profileInfo :{
            image:'defaultMale.png',
            name:'',
            age:'',
            sex:'',
            skillSet:'',
            location:'',
            price:'',
            rating:'',
            gender:'',
            jobType:''
        },
        email:''
    }
  },
  created: function(){
      
      this.email = typeof(this.$route.params.email) ==='undefined'?'':this.$route.params.email;
      this.getProfile();
  },
  methods:{
    
    getProfile: function() {
        var self = this;
        console.log("email di"+this.email);
        axios.post('api/getUsersProfile',{"emailId":this.email})
        .then(function(data){
            self.profileInfo =  data['data']['profile'];
        })
        .catch(function(errors){

        });

    }
    
  },
  computed:{

  }

}
</script>
