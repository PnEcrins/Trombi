import axios from 'axios'
import UserCard from './UserCard.vue'
import UserCalendar from './UserCalendar.vue'
export default {
    name: "trombi-cal",
    props: {
      msg: String,
    },
    components : {
        UserCard, UserCalendar
    },
    mounted() {
        axios.get(`${this.$config.API_ENDPOINT}/users_order_by_dep`).then((response) => {
            this.allUsers = response.data
            this.filteredUsers = this.allUsers;
        })
    },
    
    data() {
        return {
            'departments': {},
            'currentUser': null,
            "allUsers": {},
            "filteredUsers": {}
        }
    },
    methods : {
        setCurrentUser(person) {
            this.currentUser = person;
            this.filteredUsers = [];
        },
        setCurrDepartment(dep) {
            this.currentUser = null;
            this.curDepartment = dep;
            this.filteredUsers = {};
            Object.keys(this.allUsers).map(curDep => {
                if(dep == curDep) {
                    this.filteredUsers[dep] = this.allUsers[dep];
                }
            })
        },
        refresh() {
            this.filteredUsers = this.allUsers;
            this.currentUser = null;
        },

        changeHasPhotoProp(userLogin) {
            Object.keys(this.allUsers).forEach(dep => {
                this.allUsers[dep].forEach(user => {
                    if(userLogin == user.sAMAccountName) {
                        user.has_photo = true;
                    }
                });
            })
        }
    },

  };