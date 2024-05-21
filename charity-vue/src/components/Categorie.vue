<template>
    <h1>categorie</h1>
    <form>
        <div class="form-group">
            <label for="libelle">Libelle</label>
            <input type="email" class="form-control" id="libelle" aria-describedby="libelle">
           
        </div>
        <div class="description">
            <label for="description">Description</label>
            <input type="password" class="form-control" id="description">
        </div>
     
        <button type="submit" class="btn btn-primary">Submit</button>
</form>
</template>

<script>
    export default{
        data(){
            return {
                categorie:{},
                categories : []
            }
        },

        methods:{
            addCategorie(){
               axios.post(API_URL+ '/api/charity/categoried',  this.categorie)
               .then(response => {
                   console.log('reponse',response.data);
                   this.categorie={}
               }).catch(error => {
                   console.error('Erreur lors de la création de la categorie:', error);
               });
            },
            listCategorie(){
                axios.get(API_URL + '/api/charity/categoried')
                .then(response => {
                    console.log('reponse',response.data);
                    this.categories = response.data
                }).catch(error => {
                    console.error('Erreur lors de la récupération des categories:', error);
                });
            }
        }
    }
</script>