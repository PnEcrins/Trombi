<template>

        <div class="card-body no-padding-top">
            <h5 class="card-title" style="cursor:pointer" @click="changeUser(user)" >{{user?.displayName}}</h5>
                <div v-if="user?.description?.length > 0">
                    <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-person" viewBox="0 0 16 16">
                    <path d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm2-3a2 2 0 1 1-4 0 2 2 0 0 1 4 0zm4 8c0 1-1 1-1 1H3s-1 0-1-1 1-4 6-4 6 3 6 4zm-1-.004c-.001-.246-.154-.986-.832-1.664C11.516 10.68 10.289 10 8 10c-2.29 0-3.516.68-4.168 1.332-.678.678-.83 1.418-.832 1.664h10z"/>
                    </svg>
                        {{user?.description[0]}}
                </div>
            <div v-if="user?.homePhone && user?.homePhone?.length > 0" >
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-telephone" viewBox="0 0 16 16">
                    <path d="M3.654 1.328a.678.678 0 0 0-1.015-.063L1.605 2.3c-.483.484-.661 1.169-.45 1.77a17.568 17.568 0 0 0 4.168 6.608 17.569 17.569 0 0 0 6.608 4.168c.601.211 1.286.033 1.77-.45l1.034-1.034a.678.678 0 0 0-.063-1.015l-2.307-1.794a.678.678 0 0 0-.58-.122l-2.19.547a1.745 1.745 0 0 1-1.657-.459L5.482 8.062a1.745 1.745 0 0 1-.46-1.657l.548-2.19a.678.678 0 0 0-.122-.58L3.654 1.328zM1.884.511a1.745 1.745 0 0 1 2.612.163L6.29 2.98c.329.423.445.974.315 1.494l-.547 2.19a.678.678 0 0 0 .178.643l2.457 2.457a.678.678 0 0 0 .644.178l2.189-.547a1.745 1.745 0 0 1 1.494.315l2.306 1.794c.829.645.905 1.87.163 2.611l-1.034 1.034c-.74.74-1.846 1.065-2.877.702a18.634 18.634 0 0 1-7.01-4.42 18.634 18.634 0 0 1-4.42-7.009c-.362-1.03-.037-2.137.703-2.877L1.885.511z"/>
                </svg>
                {{user?.homePhone}}
            </div>
            <div v-if="user?.mobile && user?.mobile?.length > 0" >
                <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-phone" viewBox="0 0 16 16">
                    <path d="M11 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h6zM5 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H5z"/>
                    <path d="M8 14a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/>
                </svg>
                 {{user?.mobile}}
            </div>
            <a v-bind:href="'mailto: ' + user?.mail"  class="btn btn-primary"  title="Envoyer un email"  >
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
                    <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2zm13 2.383-4.758 2.855L15 11.114v-5.73zm-.034 6.878L9.271 8.82 8 9.583 6.728 8.82l-5.694 3.44A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.739zM1 11.114l4.758-2.876L1 5.383v5.73z"/>
                </svg>
            </a>
            <a 
                href="#/user"
                 title="Aller à la fiche"                
                 v-if="displaySeeMoreBtn" 
                @click="changeUser(user)" 
                class="btn btn-primary ml-3">
                    Détail
            </a>

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
import 'tippy.js/dist/tippy.css';

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

    .card {
    -webkit-box-shadow: 1px 1px 9px -1px rgba(0,0,0,0.6); 
    box-shadow: 1px 1px 9px -1px rgba(0,0,0,0.6);
    }

    .btn-primary {
        background-color: #42b983!important;
        border-color: #42b983!important;
    }


</style>