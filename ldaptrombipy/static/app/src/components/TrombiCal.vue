<template>
   <div id="wrapper">
        <div id="sidebar-wrapper">
          <div class="logo-container">
              <img @click="refresh()" id="logo" src="../assets/logo.png">
          </div>
            <h1 id="refresh" @click="refresh()" > {{$config.APP_NAME}} </h1>
  
            <ul class="sidebar-nav">
              <input 
                class="form form-control" 
                placeholder="Rechercher" 
                type="text" name="search" id="search"
                v-model="searchPattern" @input="filterUsers"
              >
                <li v-for="(users, dep) in filteredUsers" v-bind:key="users">
                    <div v-if="users.length > 0">
                      <a class="dep"
                        href="#"
                        @click="setCurrDepartment(dep)"
                    > 
                    {{dep}} 
                    </a> 
                        <a 
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
              <h2> Fiche {{currentUser?.displayName}} </h2>
              <div class="card mb-3">
                <div class="row g-0">
                  <div class="col-md-3">
                      <img 
                        v-if="currentUser.has_photo" :src="`${$config.API_ENDPOINT}/static/images/${currentUser?.sAMAccountName}.jpg`"
                        class="img-fluid rounded-start"
                        >
                      <img v-else src="../assets/no-photo.jpg" class="img-fluid rounded-start" alt="Pensez à ajouter une photo">
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
                <h3 > {{dep}} </h3> 
                  <div class="row">
                    <div class="card-container" v-for="user in users" v-bind:key="user">
                      <div class="card align" style="width: 18rem;">
                        <img 
                          v-if="user.has_photo" 
                          :src="`${$config.API_ENDPOINT}/static/images/${user?.sAMAccountName}.jpg`"
                          class="card-img-top"
                        >
                        <img width="250" v-else src="../assets/no-photo.jpg" class="card-img-top" alt="...">
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
  width: 15%;
  /* position: fixed; */

  height: 100vh;
  max-height: 100vh;
  overflow-y: auto;
  background-color: rgba(109, 148, 150, 0.397);
  
}

#page-content-wrapper {
  width: 85%;
  height: 100vh;
  max-height: 100vh;
  overflow-y: auto;
}

.sidebar-nav li {
    text-indent: 20px;
    line-height: 40px;
    display: block;
    
}

.sidebar-nav li a {
    display: block;
    text-decoration: none;
    color: #999999;
    cursor: pointer;
}
.sidebar-nav li a.dep{
  font-weight: bold;
  color: black;
}

.sidebar-nav li a:hover {
    text-decoration: none;
    color: #fff;
    background: rgba(255,255,255,0.2);
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
</style>
