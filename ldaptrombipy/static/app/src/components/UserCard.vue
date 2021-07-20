<template>

        <div class="card-body no-padding-top">
            <h5 class="card-title">{{user?.displayName}}</h5>
                <div v-if="user?.description?.length > 0">
                    {{user?.description[0]}}
                </div>
            <div>
                Téléphone bureau : {{user?.homePhone}}
            </div>
            <div>
                Téléphone portable : TODO 
            </div>
            <a v-bind:href="'mailto: ' + user?.mail"  class="btn btn-primary">Email</a>
            <button v-if="displaySeeMoreBtn" @click="changeUser(user)" class="btn btn-outline-info ml-3">Voir plus</button>

            <div v-if="displayAddPhoto">
                <br>
                <div v-if="$config.SELF_UPLOAD_PHOTO" class="custom-file">
                    <input @change="uploadImg" type="file" class="custom-file-input" id="customFile">
                    <label class="custom-file-label" for="customFile">Ajouter ou modifier la photo</label>
                </div>
            </div>

        </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "user-card",
    props : {
        user: Object,
        displaySeeMoreBtn: Boolean,
        displayAddPhoto: Boolean

    },
    data() {
        return {
            photoPath: null,
            has_photo: false
        }
    },
    methods: {
        changeUser(user) {
            this.$emit("setUser", user);
        },
        uploadImg(e) {
            this.photoPath = e.target.files[0];
            if(this.photoPath) {
                let fd = new FormData();
                fd.append('image', this.photoPath);
                axios.post(`${this.$config.API_ENDPOINT}/upload_photo/${this.user.sAMAccountName}`, fd)
                    .then(resp => {
                    this.imagePath = resp.data.path;
                    this.$emit('hasPhoto', this.user.sAMAccountName)
                })
            }
        }
    }


}
</script>

<style>
    .custom-file{
        width: inherit !important;;
    }

    .no-padding-top {
        padding-top: 5px!important;
    }
    .card-body div {
        margin-bottom: 5px;
    }
</style>