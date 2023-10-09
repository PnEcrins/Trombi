<template>
   <div id="wrapper">
        <div id="sidebar-wrapper">
          <div class="logo-container">
              <img @click="refresh()" id="logo" src="../assets/logo.png">
          </div>
            <h4 class="mb-3" id="refresh" @click="refresh()" > {{$config.APP_NAME}} </h4>
  
            <ul class="sidebar-nav">
              <input 
                class="form form-control mb-3" 
                placeholder="Rechercher" 
                type="text" name="search" id="search"
                v-model="searchPattern" @input="filterUsers"
              >
                <li v-for="(users, dep) in filteredUsers" v-bind:key="users">
                    <div v-if="users.length > 0">
                      <a class="dep"
                        href="#/dep"
                        @click="setCurrDepartment(dep)"
                    > 
                     <i class="fa fa-home icon"></i>
                      {{dep}} 
                    </a> 
                        <a 
                          href="#/user"
                          class="person" 
                          v-for="user in users"
                          v-bind:key="user"
                          @click="setCurrentUser(user)"
                        >
                            {{user.displayName}}

                        </a>
                    </div>

                </li>
            </ul>
        </div>
        <div id="page-content-wrapper">
          <div class="container-fluid">
            <div v-if="currentUser">
              <div class="card mb-3">
                <div class="row g-0">
                  <div class="col-md-3">
                      <img 
                        v-if="currentUser.has_photo" :src="`${$config.API_ENDPOINT}/static/images/${currentUser?.sAMAccountName}.${currentUser?.photo_extension}`"
                        class="img-fluid rounded-start"
                        >
                      <img v-else src="../assets/no-photo.png" class="img-fluid rounded-start" alt="Pensez à ajouter une photo">
                  </div>
                  <div class="col-md-9 no-padding" >
                    <UserCard 
                      :user="currentUser" 
                      @hasPhoto="changeHasPhotoProp($event)"
                      displayAddPhoto
                    />
                  </div>
                </div>
              </div>
              <div>
                <UserCalendar :user="currentUser"/>

              </div>
            </div>
            <div v-else>
              <div v-for="(users, dep) in filteredUsers" v-bind:key="users"  >
                <div v-if="users.length > 0">
                <h3 class="dep-title" > <i class="fa fa-home dep-title-logo"></i> {{dep}} </h3> 
                  <div class="row">
                    <div class="card-container" v-for="user in users" v-bind:key="user">
                      <div class="card align" style="width: 18rem;">
                        <img 
                          v-if="user.has_photo" 
                          :src="`${$config.API_ENDPOINT}/static/images/${user?.sAMAccountName}.${user?.photo_extension}`"
                          class="card-img-top"
                        >
                        <img width="250" v-else src="../assets/no-photo.png" class="card-img-top" alt="...">
                        <UserCard 
                          :user="user" 
                          @setUser="setCurrentUser($event)" 
                          displaySeeMoreBtn
                        />
                      </div>
                    </div>
                  </div>
                </div>
  

              </div>
            </div>



          </div>

        </div>
    

   </div>
</template>

<script src="./TrombiCal.js"> </script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.container-fluid {
  width: 90%!important;
}

.card-container {
    margin-right: 20px;

}

.no-padding {
  padding-left: 0px!important;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

#wrapper {
  display: flex;
}

#sidebar-wrapper{
  width: 25%;

  height: 100vh;
  max-height: 100vh;
  overflow-y: auto;
    background-color: #32323a;
    padding: 5px

  
}

#page-content-wrapper {
  width: 85%;
  height: 100vh;
  max-height: 100vh;
  overflow-y: auto;
}

.sidebar-nav li {
  line-height: 40px;
    display: block;
    
}

.person {
  text-indent: 20px;
      margin-left: -15px;
    margin-right: -15px;
}

.dep {
    margin-left: -15px;
    margin-right: -15px;
    padding-left: 5px;
}



.sidebar-nav li a {
    display: block;
    text-decoration: none;
    color: white;
    cursor: pointer;
}
.sidebar-nav li a.dep{
  font-weight: bold;
  color: #42b983;
}

.sidebar-nav li a:hover {
    text-decoration: none;
  background: #28282e;
    color: #1FB5AD;
}

.sidebar-nav li a:active,
.sidebar-nav li a:focus {
    text-decoration: none;
}

.sidebar-nav > .sidebar-brand {
    height: 65px;
    font-size: 18px;
    line-height: 60px;
}

.sidebar-nav > .sidebar-brand a {
    color: #ffffff;
}

.sidebar-nav > .sidebar-brand a:hover {
    color: #fff;
    background: none;
}
.card {
  margin-bottom: 10px;
}

#refresh {
  cursor: pointer;
}

.align img {
  align-items: center;
}

#refresh {
    width: 30%;
    margin: 0 auto;
    font-weight: bold;
    color:white
}

.icon {
  font-size: large;
}

.dep-title-logo {
    text-align: center;
    font-size: 30px;
    background: #42b983;
    border-radius: 100%;
    color: #fff;
    padding: 5px;
}

.dep-title {
    margin-left: -15px;
}

</style>
