<template>
  <div class="body">
    <div>
      <img src="~/assets/images/prepi.png" />
    </div>
    <v-app style="background-color: white; color: white">
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="d-flex flex-column text-center" color="grey lighten-5">
            <v-toolbar color="grey darken-1">
              <v-toolbar-title>Área de Acesso</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
              <form ref="form">
                <v-text-field
                  v-model="user.email"
                  height="40"
                  dense
                  persistent-hint
                  :rules="[
                    (v) => !!v || 'E-mail obrigatório',
                    (v) => /.+@.+\..+/.test(v) || 'E-mail inválido',
                  ]"
                  class="v-text-field--outlined text-black"
                  outlined
                  @keypress.enter="login"
                >
                  <template v-slot:prepend-inner>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-icon color="black" v-on="on"
                          >mdi-account-outline</v-icon
                        >
                      </template>
                      Email
                    </v-tooltip>
                  </template>
                </v-text-field>

                <v-text-field
                  v-model="user.password"
                  autocomplete="password-field"
                  height="40"
                  dense
                  persistent-hint
                  :rules="[(v) => !!v || 'Senha obrigatória']"
                  class="v-text-field--outlined text-black"
                  :append-icon="
                    show ? 'mdi-eye-outline' : 'mdi-eye-off-outline'
                  "
                  outlined
                  :type="show ? 'text' : 'password'"
                  @click:append="show = !show"
                  @keypress.enter="login"
                >
                  <template v-slot:prepend-inner>
                    <v-tooltip bottom>
                      <template v-slot:activator="{ on }">
                        <v-icon color="black" v-on="on"
                          >mdi-lock-outline</v-icon
                        >
                      </template>
                      Senha
                    </v-tooltip>
                  </template>
                </v-text-field>
                <div class="text-center justify-center">
                  <v-btn
                    type="submit"
                    class="mt-4"
                    color="grey darken-1"
                    value="log in"
                    >Acessar</v-btn
                  >
                  <div class="text-center justify-center">
                    <v-btn to="signup" class="mt-4" color="grey darken-1"
                      >Registrar</v-btn
                    >
                  </div>
                </div>
                <div class="text-right">
                  <router-link to="forgot-pass" align-center color="white"
                    >Esqueceu a Senha?</router-link
                  >
                </div>
              </form>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-app>
  </div>
</template>



<script>
export default {
  name: "Login",

  data() {
    return {
      user: {
        email: "",
        password: "",
      },
      show: false,
    };
  },
};
</script>

<style scoped>
.v-text-field--outlined >>> fieldset {
  border-color: rgba(12, 12, 12, 0.986);
}
.text-black >>> .v-text-field__slot input {
  color: black !important;
}
.body {
  overflow: hidden;
  height: 100vh;
}
</style>