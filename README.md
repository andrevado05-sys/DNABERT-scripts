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

per mascherare il dataset ho utilizzato questo script: 
masking.py

Per eseguire fine-tune:
python run_finetune.py     --model_type dna     --tokenizer_name=dna$KMER     --model_name_or_path $MODEL_PATH     --task_name dnaprom     --do_train     --do_eval     --data_dir $DATA_PATH     --max_seq_length 50     --per_gpu_eval_batch_size=2     --per_gpu_train_batch_size=2     --learning_rate 2e-4     --num_train_epochs 2.0     --output_dir $OUTPUT_PATH     --evaluate_during_training     --logging_steps 10     --save_steps 1000     --warmup_percent 0.1     --hidden_dropout_prob 0.1     --overwrite_output     --weight_decay 0.01     --n_process 1

per visualizzare i dati di output per il finetune: 
finetuneresult.py

i datate set per la validazione biologica: notatahg38_KzawA.fa.txt,tatahg38_fYp4B.fa.txt
