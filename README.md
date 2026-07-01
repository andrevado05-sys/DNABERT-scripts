# DNABERT-prompts
Questo repository contiene la pipeline sperimentale, gli script di configurazione e i log di addestramento sviluppati per la tesi di laurea incentrata sul fine-tuning e sulla validazione biologica del modello linguistico genomico **DNABERT** applicato ai promotori umani.

Per preparare l'ambiente di lavoro seguire il punto 1 dalla seguente repository.
https://github.com/jerryji1993/DNABERT
Per scaricare il modello pre addestrato, vedere il read_me sempre di questa repository e scegliere il k-mer desiderato. Vi porterà sulla pagina di huggingface.

Per calcolare perplexity:
python3 run_pretrain.py \
    --model_type bert \
    --model_name_or_path [Indirizzo modello]
    --do_eval \
    --train_data_file [Indirizzo Data]
    --eval_data_file [Indirizzo Data]
    --output_dir [Indirizzo output]
    --mlm \
    --line_by_line \
    --overwrite_output_dir \
    --no_cuda

