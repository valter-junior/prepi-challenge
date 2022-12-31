<template>
  <v-container class="fluid fill-height">
    <div class="d-flex flex-column justify-center align-center text-center">
      <img src="~/assets/images/prepi.png" />
    </div>

    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-12">
          <v-form ref="form">
            <v-text-field
              v-model="user.email"
              height="40"
              dense
              :rules="[
                (v) => !!v || 'E-mail obrigatório',
                (v) => /.+@.+\..+/.test(v) || 'E-mail inválido',
              ]"
              class="primary-input"
              prepend-inner-icon="mdi-account-outline"
              outlined
              @keypress.enter="login"
            ></v-text-field>
            <v-text-field
              v-model="user.password"
              autocomplete="password-field"
              height="40"
              dense
              :rules="[(v) => !!v || 'Senha obrigatória']"
              class="primary-input"
              prepend-inner-icon="mdi-lock-outline"
              :append-icon="show ? 'mdi-eye-outline' : 'mdi-eye-off-outline'"
              outlined
              :type="show ? 'text' : 'password'"
              @click:append="show = !show"
              @keypress.enter="login"
            ></v-text-field>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>