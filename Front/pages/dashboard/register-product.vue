<template>
  <div>
    <DashboardComponent />

    <div class="body">
      <v-row justify="center" align="center">
        <v-card
          class="d-flex flex-column justify-center text-center"
          color="grey lighten-5"
          width="500"
          title="Product Registration"
        >
          <v-toolbar height="55" color="grey darken-1">
            <v-toolbar-title class="justify-center text-center"
              >Cadastrar Produto</v-toolbar-title
            >
          </v-toolbar>
          <v-container>
            <v-col>
              <v-text-field
                v-model="register.name"
                color="black"
                label="Nome"
                :rules="[(v) => !!v || 'Nome obrigatório']"
                light
                variant="underlined"
                class="v-text-field--outlined text-black"
                outlined
              ></v-text-field>

              <v-text-field
                v-model="register.quantity"
                color="black"
                light
                label="Quantidade"
                variant="underlined"
                class="v-text-field--outlined text-black"
                type="number"
                outlined
              ></v-text-field>

              <v-currency-field
                v-model="register.value"
                color="black"
                light
                label="Valor Unitário"
                :error-messages="erros.rate"
                variant="underlined"
                outlined
              />
            </v-col>
          </v-container>
          <v-card-actions class="text-center justify-center">
            <v-btn to="/dashboard" color="grey darken-1">
              Registrar
              <v-icon icon="mdi-chevron-right" end></v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-row>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      register: {
        name: "",
        quantity: 0,
        value: 0,
      },
      erros: {},
    };
  },
};
</script>

<style scoped>
.body {
  padding: 60px;
  height: 12%;
  align-content: center;
  justify-content: center;
}
</style>