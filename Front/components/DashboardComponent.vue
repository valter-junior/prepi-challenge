<template>
  <div id="app">
    <v-menu bottom min-width="200px" rounded offset-y>
      <template v-slot:activator="{ on }">
        <v-btn icon x-large v-on="on">
          <v-avatar>
            <span class="white--text text-h5">{{
            }}</span>
            <span
              ><v-img
                max-height="48"
                max-width="48"
                src="~/assets/images/prepi.png"
              ></v-img
            ></span>
          </v-avatar>
        </v-btn>
      </template>
      <v-card>
        <v-list-item-content class="justify-center">
          <div class="mx-auto text-center">
            <v-avatar dark color="black">
              <span class="white--text text-h5">{{
              }}</span>
              <span
                ><v-img
                  max-height="48"
                  max-width="48"
                  src="~/assets/images/prepi.png"
                ></v-img
              ></span>
            </v-avatar>

            <p class="text-caption mt-1">Olá, </p>
            <p class="text-caption mt-1">
            </p>

            <v-divider class="my-3"></v-divider>
            <v-btn depressed rounded text to="profile-user">
              Edit Account
            </v-btn>
            <v-divider class="my-3"></v-divider>
            <v-btn depressed rounded text href="home" >
              Log out
            </v-btn>
          </div>
        </v-list-item-content>
      </v-card>
    </v-menu>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  data() {
    return {
      imagepath: null,
      initials: "va",
      name: "",
      email: "",
      path: ''
    };
  },
};