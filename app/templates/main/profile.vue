<template>
    <div class="container-fluid mb-2">
        <div class="row">
            <div class="col-md-8 col-lg-8 col-md-offset-2 mt-3 mb-3">
                <div class="page-wrap profile account well well-sm">
                    <div class="row">
                        <div class=" col-md-4 col-lg-4 col-md-offset-1 page-header">
                            <div class="row">
                                <div class="art solo-art profile-art">
                                    <img v-bind:src="'images/'+profileInfo.image" >
                                </div>
                            </div>
                            <div class="row mt-2" v-if="editingEnabled">
                                <form enctype="multipart/form-data" action="/profile" method="post" id="submitForm">
                                    <input name="file" type="file" id="fileUpload"  class="upload-file"   accept=".jpg, .png, .jpeg, .gif, .bmp, .tif, .tiff|images/*"  />
                                    <input type="submit" value="Upload">
                                </form>
                            </div>
                        </div>
                        <div class=" col-md-5 col-lg-5">
                            <div class="row mt-2 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Name</h5>
                                </div>
                                <div class="col-md-6">
                                    <span v-if="!editingEnabled" class="heading h6">{{profileInfo.name}}</span>
                                    <input v-else type="text" placeholder="Enter Display Name" required v-model="profileInfo.name" class="form-control">
                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Sex</h5>
                                </div>
                                <div class="col-md-6">
                                    <span v-if="!editingEnabled" class="heading h6">{{profileInfo.sex}}</span>
                                    <span v-else>
                                        <input type="radio" id="male" value="Male" v-model="profileInfo.sex">
                                        <label for="Male">Male</label>

                                        <input type="radio" id="female" value="Female" v-model="profileInfo.sex">
                                        <label for="Female">Female</label>
                                    </span>
                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">

                                    <h5 class="h5Label">Age</h5>
                                </div>
                                <div class="col-md-6">
                                    <span v-if="!editingEnabled" class="heading h6">{{profileInfo.age}}</span>
                                    <input v-else type="number" min=1 v-model="profileInfo.age" placeholder="Enter Age" class="form-control">
                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Job Type</h5>
                                </div>
                                <div class="col-md-6">
                                    <span v-if="!editingEnabled" class="heading h6">{{profileInfo.jobType}}</span>
                                    <select v-else type="text" placeholder="Enter Location" required v-model="profileInfo.jobType" class="form-control">
                                        <option value="FullTime">FullTime</option>
                                        <option value="PartTime">PartTime</option>
                                    </select>
                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Location</h5>
                                </div>
                                <div class="col-md-6">
                                    <span v-if="!editingEnabled" class="heading h6">{{profileInfo.location}}</span>
                                    <input v-else type="text" placeholder="Enter Location" required v-model="profileInfo.location" class="form-control">
                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">
                                    <h5 class="h5Label">Skill Sets</h5>
                                </div>
                                <div class="col-md-6">
                                    <span v-if="!editingEnabled" class="heading h6">{{profileInfo.skillSet}}</span>
                                    <input v-else type="text" v-model="profileInfo.skillSet" required placeholder="Enter Skill seperated by comma" class="form-control">
                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">

                                    <h5 class="h5Label">Price $(Per Hour)</h5>
                                </div>
                                <div class="col-md-6">
                                    <span v-if="!editingEnabled" class="heading h6">{{profileInfo.price}}</span>
                                    <input v-else type="number" v-model="profileInfo.price" placeholder="Enter Price per hour" class="form-control">
                                </div>
                            </div>
                            <div class="row mt-1 mb-2">
                                <div class="col-md-6">

                                    <h5 class="h5Label">Rating</h5>
                                </div>
                                <div class="col-md-6">
                                    <span v-if="!editingEnabled" class="heading h6">{{profileInfo.rating}}</span>
                                    <input v-else type="number" min="1" max="5" placeholder="Enter rating (1-5)" v-model="profileInfo.rating" class="form-control">
                                </div>
                            </div>
                        </div>

                    </div>
                    <div class="row mt-2">
                        <div class="col-md-3 col-lg-3 col-md-offset-5">

                            <button v-if="!editingEnabled" class="btn btn-primary" @click="enableEditing()">Edit</button>
                            <button v-if="editingEnabled" type="submit" class="btn btn-success" @click="updateProfile()">Save</button>
                            <button v-if="editingEnabled" class="btn btn-danger" @click="resetProfile()">Reset</button>

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
        editingEnabled :false,
        profileInfo :{
            image:'default.png',
            name:'',
            age:'',
            sex:'',
            skillSet:'',
            location:'',
            price:'',
            rating:'',
            gender:'',
            jobType:''
        }
    }
  },
  created: function(){
      this.getProfile();
  },
  methods:{
    enableEditing : function(){
        this.editingEnabled = ! this.editingEnabled;
    },
    getProfile: function() {
        var self = this;
        axios.get('api/saveProfile')
        .then(function(data){
            self.profileInfo =  data['data']['profile'];
        })
        .catch(function(errors){

        });

    },
    updateProfile:function(){
        this.editingEnabled = ! this.editingEnabled;

        axios.post("api/saveProfile",{profile:this.profileInfo})
            .then(function(data){
                if(data['data']['status']==0)
                    alert("Please fill out all the fields");
            })
            .catch(function(error){
                
            });
    },
    resetProfile:function(){
        this.editingEnabled = ! this.editingEnabled;
    }
  },
  computed:{

  }

}
</script>
