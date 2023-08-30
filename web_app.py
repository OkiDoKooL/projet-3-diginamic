import streamlit as st
import pandas as pd
import pickle
import json
import numpy as np




# Chargement de tous les objets nécéssaire : encodeurs, scalers, modèles


filename_model = 'regression_opti.pkl'
model_reg_opti = pickle.load(open(filename_model,'rb'))

print('Modèle de Régression Chargé !')

filename_model_classification = 'classification_opti.pkl'
model_clas_opti = pickle.load(open(filename_model_classification, 'rb'))

print('Modèle de Classification Chargé !')


filename_encoder_ss = 'encoder_sugarscale.pkl'
encoder_sugar_scale = pickle.load(open(filename_encoder_ss,'rb'))

filename_ohe = 'ohe_brew.pkl'
encoder_ohe = pickle.load(open(filename_ohe,'rb'))

print('Encodeurs Chargés !')

filename_scaler = 'scaler.pkl'
scaler = pickle.load(open(filename_scaler,'rb'))

print('Scaler Chargé !')

filename_imputer_cat = 'imputer_cat.pkl'
imputer_cat = pickle.load(open(filename_imputer_cat,'rb'))

filename_imputer_numerique = 'imputer_numerique.pkl'
imputer_num = pickle.load(open(filename_imputer_numerique,'rb'))

print('Imputeurs Chargés !')

# Définitions des listes utiles à nos traitements

liste_variables_numerique = ['Color', 'BoilTime', 'Efficiency', 'PrimaryTemp', 'diff_densite_fermentation', 'qte_eau_litre_biere' ]
liste_variables_qualitatives_ohe = ['Style', 'BrewMethod']
liste_variables_qualitatives_le = ['SugarScale']
liste_variable_qualitatives = liste_variables_qualitatives_ohe + liste_variables_qualitatives_le







st.title("Maîtres Brasseurs de Pandarie")
st.write("Bienvenue à toi brasseur ! Que tu sois jeune ou expérimenté, te voilà au bon endroit !")
st.write("En ces lieux, tu peux recenser une recette expérimentale de bière, déjà produite ou non, et nous te donnerons son degré d'alcool : ABV; ainsi qu'une étiquette variant de 0 à 4, correspondant à son amertume !")

st.write("Tu penses que c'est de la magie ?")


data = st.file_uploader("Charger le json de la recette à tester", type = 'json')


if data is not None:
    st.write('Chargement du json réussi !')
    data = data.read().decode('utf-8')
    data = json.loads(data)
    st.write('Chargement du json réussi !')
#if data is not None :
#    st.write('Bien reçu ! : Début du traitement')
    
#    data = json.loads(data)
    
    
    
    df_json = pd.DataFrame(data, index= [0])
    
    # Suppression des variables qui ne nous interessent pas
    
    df_json = df_json.drop(
    ["PrimingAmount", "PrimingMethod", "UserId", "PitchRate", "MashThickness", "BeerID", "Name", "URL", "StyleID", "BoilGravity", 'IBU', 'ABV'], axis=1
)
    
    for col in df_json.columns:
    
        if df_json[col][0] is None :
            
            df_json[col][0] = np.nan
    
    
    
    val = df_json['PrimaryTemp'][0]
    
    if  val < 0  :
        
        df_json['PrimaryTemp'][0] = np.nan
        
    # Création de la variable correspondant à la différence de densité entre la fin et le début de la fermentation
    
    df_json["diff_densite_fermentation"] = df_json["FG"] - df_json["OG"]
    
    df_json = df_json.drop(['FG', 'OG'], axis = 1)
    
    
    # Création de la variable relative à la quantité d'eau utilisée pour brasser un litre de bière
    
    df_json["qte_eau_litre_biere"] = df_json["BoilSize"] / df_json["Size(L)"]
    
    
    df_json = df_json.drop(['BoilSize', 'Size(L)'], axis = 1)
    
    # Message pour l'utilisateur s'il renseigne mal cette variable
    
    if 1 / 3 <= df_json["qte_eau_litre_biere"][0] <= 3:
        
        st.write("Très bien, la quantité d'eau nécéssaire pour fabriquer un litre de bière est dans la plage appropriée.")
    else:
        st.write("Avertissement : La quantité d'eau nécessaire pour fabriquer un litre de bière est hors de la plage recommandée, cela pourrait affecter les prédictions.")
    
    # lowercase + retrait des espaces inutiles en début et fin de chaines de caractères
    
    df_json["Style"] = df_json["Style"].str.lower().str.strip()
    
    # Imputation
    
    df_json[liste_variables_numerique] = imputer_num.transform(df_json[liste_variables_numerique])

    
    df_json[liste_variable_qualitatives] = imputer_cat.transform(df_json[liste_variable_qualitatives])
    
    
    # Encodage
    
    df_json["SugarScale"] = encoder_sugar_scale.transform(df_json['SugarScale'])  # LabelEncoder
    
    
    codes_json = encoder_ohe.transform(df_json[liste_variables_qualitatives_ohe]).toarray()
    feature_names_json = encoder_ohe.get_feature_names_out()
    
    
    df_json_encoded = pd.DataFrame(codes_json,columns=feature_names_json).astype(int)
    
    df_json = pd.concat([df_json, df_json_encoded], axis=1)  # Jointure pour récupèrer les encodages OHE
    
    df_json = df_json.drop(['BrewMethod', 'Style'], axis = 1)
    
    
    st.dataframe(df_json)
    
    pred_reg_abv = model_reg_opti.predict(df_json)[0]
    
    pred_class_ibu = model_clas_opti.predict(df_json)[0]
    
    
    
    st.write(f"Le degré d'alcool de ta recette est {pred_reg_abv} !")
    
    
    if pred_class_ibu == 0 :
        
        st.write(f"Ta bière sera peu amère ! Classe = {pred_class_ibu}")
    
    elif pred_class_ibu == 1 :
        
        st.write(f"Ta bière aura une amertume modérée ! Classe = {pred_class_ibu}")
        
    elif pred_class_ibu == 2 :
        
        st.write(f"Ta bière aura une amertume prononcée ! Classe = {pred_class_ibu}")
    
    elif pred_class_ibu == 3:
        
        st.write(f"Ta bière aura une amertume intense ! Classe = {pred_class_ibu}")
    
    else:
        
        st.write(f"Ta bière aura une amertume très intense ! Classe = {pred_class_ibu}")
    
    
    
    
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



#st.json(recette)